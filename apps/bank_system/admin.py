from django.contrib import admin

from apps.bank_system.models import User, HistoryTransfer
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'phone_number', 'created_at', 'age', 'wallet_address')

@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display=('from_user', 'to_user', 'is_completed', 'created_at', 'amount')