from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15, 
        unique=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    age = models.PositiveIntegerField(
        null=True, 
        blank=True
        )
    wallet_address = models.CharField(
        max_length=12, 
        unique=True, 
        default=random.randint(100000000000,999999999999), 
        editable=False)

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
        return self.username
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
