from django.contrib import admin

from apps.bank_system.models import HistoryTransfer

# Register your models here.
@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display=('from_user', 'to_user', 'is_completed', 'created_at', 'amount')