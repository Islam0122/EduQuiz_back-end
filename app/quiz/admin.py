from django.contrib import admin
from .models import Topic, Question


class QuestionInline(admin.TabularInline):  # или StackedInline для вертикального отображения
    model = Question
    extra = 1  # Количество пустых полей для добавления новых вопросов
    readonly_fields = ("created_at", "updated_at")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty", "is_active", "created_at", "create_user")
    list_filter = ("difficulty", "is_active", "created_at")
    search_fields = ("name", "description")
    ordering = ("-created_at",)
    list_editable = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
    inlines = [QuestionInline]  # Позволяет редактировать вопросы внутри темы
    fieldsets = (
        ("Основная информация", {"fields": ("name", "description", "difficulty", "is_active")}),
        ("Дополнительная информация", {"fields": ("create_user", "created_at", "updated_at")}),
    )


# # Опционально: изменить заголовки в админке
# admin.site.site_header = "Админка Викторины"
# admin.site.site_title = "Управление Викториной"
# admin.site.index_title = "Добро пожаловать в панель администратора!"
