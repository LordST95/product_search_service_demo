from rest_framework.generics import (
    CreateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Product
from api.serializers import (
    ProductCreateSerializer, ProductListSerializer
)
from api.filters import ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    filterset_class = ProductFilter
    
    
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    # throttle_classes = [UserRateThrottle]
    # permission_classes = [IsAuthenticated]    # as its default behavior, there is no need to define it
