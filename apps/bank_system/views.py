from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import generics
from .models import User, HistoryTransfer
from apps.bank_system.serializers import UserRegisterSerializer, UserSerializer, UserDetailSerializer
from apps.bank_system.permissions import UserPermission
from .serializers import UserSerializer, HistoryTransferSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TransferMoneyView(generics.CreateAPIView):
    serializer_class = HistoryTransferSerializer
    # permission_classes = [IsAuthenticated]

class HistoryTransferView(generics.ListAPIView):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer
    # permission_classes = [IsAuthenticated]
