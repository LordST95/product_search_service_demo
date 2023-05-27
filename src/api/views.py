from rest_framework.generics import (
    CreateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, GenericAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from api.models import CartItem, Product, Cart
from api.serializers import (
    ProductCreateSerializer, ProductListSerializer,
    CartSerializer
)
from api.filters import ProductFilter


class ProductListView(ListAPIView):
    """
    search in all products
    
    you can search by some fields of Product model + sort parameter
    
    sort can be like <field_name> for ascending or -<field_name> for descending order
    
    example:
        GET /api/v1/products/?name=&category=&brand=&price__gte=&price__lte=&quantity__gte=2&quantity__lte=&created_at=&rating=&sort=-quantity
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [AllowAny]
    filterset_class = ProductFilter
    # throttle_classes = [AnonRateThrottle] / [UserRateThrottle] TODO, decide about it
    
    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get("sort", None)
        fields = [field.name for field in Product._meta.fields]
        fields.remove("image")
        sorting_rules = fields + [f"-{field}" for field in fields]
        if sort in sorting_rules:
            queryset = queryset.order_by(sort)
        return queryset


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class CartListView(ListAPIView):
    serializer_class = CartSerializer
    
    def get_queryset(self):
        queryset = Cart.objects.filter(buyer=self.request.user)
        return queryset


class CartCreateUpdateView(APIView):
    """
    the philosophy of this view is that we should have only one
    unpaid cart at the moment, so there's no need to know the id of that one.
    
    this view will update the unpaid cart by two parameters:
        - add, which contains a products' id willing to be added to cart
        - remove, which contains a products' id willing to be remoed from cart
    
    example:
        GET /api/v1/orders/create_update_unpaid_cart/?add=1,2&remove=4
    """

    def get(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(
            buyer=request.user, is_paid=False
        )
        add_list = request.GET.get("add", None)
        remove_list = request.GET.get("remove", None)
        
        added_list = []
        if add_list:
            for product_id in str(add_list).split(","):
                try:
                    product = Product.objects.get(id=int(product_id))
                except Product.DoesNotExist:
                    continue
                if product.quantity > 0:
                    product.quantity -= 1
                    product.save()
                    cart_item = CartItem.objects.create(cart=cart, product=product)
                    added_list.append(product.id)
        removed_list = []
        if remove_list:
            for product_id in str(remove_list).split(","):
                try:
                    product = Product.objects.get(id=int(product_id))
                except Product.DoesNotExist:
                    continue
                if CartItem.objects.filter(cart=cart, product=product).exists():
                    cart_item = CartItem.objects.filter(cart=cart, product=product)[0].delete()
                    product.quantity += 1
                    product.save()
                    removed_list.append(product.id)
        
        
        return Response(
                status=status.HTTP_200_OK,
                data={
                    "added_list": added_list,
                    "removed_list": removed_list,
                    "new_cart": CartSerializer(cart).data,
                }
            )


class CartMarkAsPaidView(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        _id = kwargs.get("pk")
        try:
            cart = Cart.objects.get(id=_id, buyer=user)
            cart.is_paid = True
            cart.save()
            message = "Cart marked as paid"
            new_cart = CartSerializer(cart).data
        except Cart.DoesNotExist:
            message = "It's not possible to mark this cart as paid"
            new_cart = None
        
        return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": message,
                    "new_cart": new_cart,
                }
            )


class CartDetailView(RetrieveAPIView):
    serializer_class = CartSerializer
    
    def get_queryset(self):
        queryset = Cart.objects.filter(buyer=self.request.user)
        return queryset

