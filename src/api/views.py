from rest_framework.generics import (
    CreateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, GenericAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.models import Product, Cart
from api.serializers import (
    ProductCreateSerializer, ProductListSerializer,
    CartListSerializer
)
from api.filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [AllowAny]
    filterset_class = ProductFilter
    # throttle_classes = [AnonRateThrottle] / [UserRateThrottle] TODO, decide about it
    
    
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class CartListView(ListAPIView):
    serializer_class = CartListSerializer
    
    def get_queryset(self):
        queryset = Cart.objects.filter(buyer=self.request.user)
        return queryset


class CartCreateUpdateView(APIView):
    """
    the philosophy of this view is that we should have only one
    unpaid cart at the moment, so there's no need to know the id of that one.
    """

    # def post(self, request):
    #     username = request.data['username']
    #     password = request.data['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         token, isCreated = Token.objects.get_or_create(user=user)
    #         return Response(
    #             status=status.HTTP_201_CREATED,
    #             data={
    #                 'token': token.key,
    #                 'user_id': user.pk,
    #                 'email': user.email
    #             }
    #         )
    #     else:
    #         return Response(
    #             status=status.HTTP_400_BAD_REQUEST,
    #             data={
    #                 'khata': "info haii ke dadi qalat bood, ia user vojood nadasht"
    #             }
    #         )


# class CartUpdateView(APIView):
#     """
#     the philosophy of this view is that we should have only one
#     unpaid cart at the moment, so there's no need to know the id of that one.
#     """


class CartMarkPaidView(UpdateAPIView):
    pass


class CartDetailView(RetrieveAPIView):
    pass
