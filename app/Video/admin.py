from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'created_at', 'is_active')
    search_fields = ('title', 'video_url')
    list_filter = ('created_at', 'is_active')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'video_url',  'is_active')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)

admin.site.register(Video, VideoAdmin)
