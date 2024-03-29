from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('users', UserAPIViewSet, 'api_users')

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name="api_user_login"),
    path('user/refresh/', TokenRefreshView.as_view(), name="api_user_refresh"),
]

urlpatterns += router.urls