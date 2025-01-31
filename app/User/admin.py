from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'fullname', 'role', 'is_allowed', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'fullname')
    list_filter = ('role', 'is_allowed', 'is_active', 'is_staff')
    readonly_fields = ('date_joined',)
    filter_horizontal = ()
    filter_vertical = ()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(obj.password)
        obj.save()

    fieldsets = (
        (None, {'fields': ('username', 'password', 'fullname', 'role', 'is_allowed', 'is_active', 'is_staff')}),
        ('Дополнительные параметры', {'fields': ('date_joined',)}),
    )

admin.site.register(User, CustomUserAdmin)
