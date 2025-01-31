from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Поле Username обязательно для заполнения')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Role.ADMIN)  # Роль суперпользователя
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # Определяем роли
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        USER = 'user', 'Пользователь'

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Введите уникальное имя пользователя для входа в систему."
    )
    fullname = models.CharField(
        max_length=30,
        blank=True,
        help_text="Полное имя пользователя. Это поле не обязательное."
    )
    is_allowed = models.BooleanField(
        default=True,
        help_text="Отметьте, если пользователь имеет доступ к системе."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Если активен, пользователь может войти в систему."
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Если отмечено, пользователь является администратором сайта."
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
        help_text="Роль пользователя в системе."
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
