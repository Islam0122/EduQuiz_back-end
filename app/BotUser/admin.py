from django.contrib import admin
from .models import BotUser

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "name", "username", "is_admin")
    list_filter = ("is_admin",)
    search_fields = ("telegram_id", "name", "username")
    ordering = ("-telegram_id",)
    readonly_fields = ("created_at", "updated_at",)

