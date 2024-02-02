from django.db import models
from apps.users.models import User
# Create your models here.
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='transfers_sent'
        )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='transfers_received'
        )
    is_completed = models.BooleanField(
        default=False
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    
    def __str__(self) -> str:
        return self.from_user - self.to_user
    
    class Meta:
        verbose_name="Историе"
        verbose_name_plural="История"
