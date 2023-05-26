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
    path('orders/add_to_unpaid_cart/', views.CartCreateUpdateView.as_view(),
         name="add_to_unpaid_cart"),
    path('orders/remove_from_unpaid_cart/', views.CartUpdateView.as_view(),
         name="remove_from_unpaid_cart"),
    path('orders/mark_cart_as_paid/<int:pk>/', views.CartMarkPaidView.as_view(),
         name="mark_cart_as_paid"),
    path('orders/detail/<int:pk>/', views.CartDetailView.as_view(),
         name="cart_detail"),

]
