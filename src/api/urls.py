from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api import views


urlpatterns = [
    # Product
    path('products/', views.ProductListView.as_view(), name='all_products'),
    # path('products/create/', views.ProductCreateView.as_view()),
    # path('products/<int:pk>/', views.ProductDetailUpdateView.as_view()),
    # path('products/special_image_changer/<int:pk>/', views.ProductDetailUpdateView.as_view()),
    
    # Orders
    path('orders/all/', views.CartListView.as_view(),
         name="all_carts"),
    path('orders/create_update_unpaid_cart/', views.CartCreateUpdateView.as_view(),
         name="create_update_unpaid_cart"),
    path('orders/mark_cart_as_paid/<int:pk>/', views.CartMarkAsPaidView.as_view(),
         name="mark_cart_as_paid"),
    # path('orders/detail/<int:pk>/', views.CartDetailView.as_view(),
    #      name="cart_detail"),

]
