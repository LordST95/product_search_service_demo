from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api import views


urlpatterns = [
    # Product
    path('products/', views.ProductListView.as_view(), name='all_products'),
    # path('products/create/', views.ProductCreateView.as_view()),
    # path('products/<int:pk>/', views.ProductDetailUpdateView.as_view()),
    # path('products/special_image_changer/<int:pk>/', views.ProductDetailUpdateView.as_view()),

]
