from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, QuestionViewSet

# Создаем роутер
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # Регистрируем вьюсет для категорий
router.register(r'questions', QuestionViewSet)  # Регистрируем вьюсет для вопросов

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты в основной файл URL
]
