from django.contrib import admin
from .models import Group, Student

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1
    fields = ('full_name','group', 'is_active', 'create_user')
    readonly_fields = ('created_at', 'updated_at', 'create_user')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'create_user')
    list_filter = ('created_at', 'create_user')
    search_fields = ('name',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'create_user')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'create_user')
    inlines = [StudentInline]

admin.site.register(Group, GroupAdmin)
