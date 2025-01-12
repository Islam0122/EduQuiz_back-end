from django.contrib import admin
from .models import Category, Question


# Инлайн форма для добавления вопросов в категории
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question_text', 'answer')
    verbose_name = "Вопрос"
    verbose_name_plural = "Вопросы"


# Настройка отображения в админке для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'question_count')
    list_filter = ('name',)
    search_fields = ('name', 'description')

    # Функция для отображения количества вопросов в категории
    def question_count(self, obj):
        return obj.questions.count()

    question_count.short_description = 'Количество вопросов'

    # Добавляем инлайн форму для вопросов
    inlines = [QuestionInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )


# Настройка отображения в админке для модели Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'short_answer')
    list_filter = ('category',)
    search_fields = ('question_text', 'answer')

    def short_answer(self, obj):
        return obj.answer[:50] + "..." if len(obj.answer) > 50 else obj.answer

    short_answer.short_description = 'Краткий ответ'

    fieldsets = (
        (None, {
            'fields': ('category', 'question_text', 'answer')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('category', 'question_text', 'answer')
        }),
    )


# Регистрация моделей с кастомными настройками
admin.site.register(Category, CategoryAdmin)
