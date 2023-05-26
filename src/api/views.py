from rest_framework.generics import (
    CreateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, GenericAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Product, Cart
from api.serializers import (
    ProductCreateSerializer, ProductListSerializer
)
from api.filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [AllowAny]
    filterset_class = ProductFilter
    
    
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    # throttle_classes = [UserRateThrottle]
    # permission_classes = [IsAuthenticated]    # as its default behavior, there is no need to define it


class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [AllowAny]
    filterset_class = ProductFilter


class CartCreateUpdateView(APIView):
    """
    the philosophy of this view is that we should have only one
    unpaid cart at the moment, so there's no need to know the id of that one.
    """
    permission_classes = (AllowAny,)    # TODO, farq e in ba authentication_classes chie ...
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, isCreated = Token.objects.get_or_create(user=user)
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'khata': "info haii ke dadi qalat bood, ia user vojood nadasht"
                }
            )


class CartUpdateView(APIView):
    """
    the philosophy of this view is that we should have only one
    unpaid cart at the moment, so there's no need to know the id of that one.
    """
    permission_classes = (AllowAny,)    # TODO, farq e in ba authentication_classes chie ...
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]


class CartMarkPaidView(UpdateAPIView):
    pass


class CartDetailView(RetrieveAPIView):
    pass
