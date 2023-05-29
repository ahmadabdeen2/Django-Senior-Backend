from django.urls import path, include
from .views import UserModelViewSet, KeystrokeTokenObtainPairView, UserCreationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', UserModelViewSet, basename='user')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # path('login/', KeystrokeAuthView.as_view(), name='login'),
    path('register/', UserCreationView.as_view(), name='register'),
    path('token/', KeystrokeTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
