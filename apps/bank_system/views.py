from rest_framework import generics
from .models import HistoryTransfer
from .serializers import HistoryTransferSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class TransferMoneyView(generics.CreateAPIView):
    serializer_class = HistoryTransferSerializer
    # permission_classes = [IsAuthenticated]

class HistoryTransferView(generics.ListAPIView):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
    # permission_classes = [IsAuthenticated]
