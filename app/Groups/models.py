from django.db import models
from app.User.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата и время создания записи.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата и время последнего обновления записи.'
    )
    create_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель записи',
        help_text='Пользователь, создавший эту запись.'
    )

    class Meta:
        abstract = True

class Group(BaseModel):
    name = models.CharField(
        max_length=150,
        verbose_name='Название группы',
        help_text='Введите название группы (до 150 символов).'
    )

    class Meta:
        db_table = 'groups'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

class Student(BaseModel):
    full_name = models.CharField(
        max_length=150,
        verbose_name='ФИО студента',
        help_text='Введите полное имя студента (до 150 символов).'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Активность студента',
        help_text='Отметьте, если студент активен в системе.'
    )

    class Meta:
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.full_name
