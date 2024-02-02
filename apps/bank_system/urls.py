from django.urls import path
from .views import TransferMoneyView, HistoryTransferView



urlpatterns = [
    path('transfer/', TransferMoneyView.as_view(), name='transfer-money'),
    path('history/', HistoryTransferView.as_view(), name='transfer-history'),
]
