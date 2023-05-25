from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts import views


urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # used for login
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("user_info/", views.UserInfoView.as_view(), name='user_info')
]
