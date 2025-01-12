from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории (например, 'JavaScript', 'Python')."
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name="Категория",
        help_text="Выберите категорию для этого вопроса."
    )
    question_text = models.TextField(
        verbose_name="Текст вопроса",
        help_text="Введите текст вопроса, который будет отображаться студентам."
    )
    answer = models.TextField(
        verbose_name="Ответ на вопрос",
        help_text="Введите правильный ответ на вопрос."
    )

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
