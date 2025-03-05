from django.db import models

class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")
    name = models.CharField(max_length=100, verbose_name="Имя")
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name="Юзернейм")
    is_admin = models.BooleanField(default=False, verbose_name="Администратор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name or f"User {self.telegram_id}"

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"
