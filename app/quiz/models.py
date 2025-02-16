from django.db import models
from app.User.models import User


class Topic(models.Model):
    """Модель для хранения тем (например, Python, HTML, CSS)"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Легкий'),
        ('medium', 'Средний'),
        ('hard', 'Сложный'),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="Название темы")
    description = models.TextField(blank=True, null=True, verbose_name="Описание темы")
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default='medium', verbose_name="Сложность"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активна ли тема")
    create_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель темы',
        help_text='Пользователь, создавший эту тему.'
    )

    def __str__(self):
        return f"{self.name} ({self.get_difficulty_display()})"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Question(models.Model):
    """Модель для вопросов"""
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="questions", verbose_name="Тема"
    )
    image = models.ImageField(upload_to='questions_images/', null=True, blank=True, verbose_name="Изображение")
    text = models.TextField(verbose_name="Текст вопроса")

    option_a = models.CharField(max_length=255, verbose_name="Вариант A")
    option_b = models.CharField(max_length=255, verbose_name="Вариант B")
    option_c = models.CharField(max_length=255, verbose_name="Вариант C")
    option_d = models.CharField(max_length=255, verbose_name="Вариант D")

    correct_answer = models.CharField(
        max_length=1,
        choices=[('A', 'Вариант A'), ('B', 'Вариант B'), ('C', 'Вариант C'), ('D', 'Вариант D')],
        verbose_name="Правильный ответ"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активен ли вопрос")

    create_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель вопроса',
        help_text='Пользователь, создавший этот вопрос.'
    )

    def __str__(self):
        return f"{self.text[:50]}..."

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
