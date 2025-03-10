from django.db import models
import random
import string
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    email = models.EmailField(verbose_name="Email пользователя")
    code = models.CharField(max_length=6, verbose_name="OTP код")  # OTP код
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания OTP")

    def __str__(self):
        return f"OTP для {self.email}"

    def is_valid(self):
        return self.created_at > timezone.now() - timedelta(minutes=15)
