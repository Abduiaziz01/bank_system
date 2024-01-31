from django.urls import path
from .views import TransferMoneyView, HistoryTransferView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.bank_system.views import UserAPIViewSet


router = DefaultRouter()
router.register('user', UserAPIViewSet, 'api_users')

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name="api_user_login"),
    path('user/refresh/', TokenRefreshView.as_view(), name="api_user_refresh"),
    path('transfer/', TransferMoneyView.as_view(), name='transfer-money'),
    path('history/', HistoryTransferView.as_view(), name='transfer-history'),
]

urlpatterns += router.urls
