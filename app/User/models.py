from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

class User(AbstractUser):
    fullname = models.CharField(max_length=255, verbose_name="Полное имя")
    is_allowed = models.BooleanField(default=True, verbose_name="Разрешен")

    def set_random_password_and_notify(self):
        """Генерирует временный пароль, устанавливает его и отправляет email"""
        password = get_random_string(10)  # Генерируем случайный пароль из 10 символов
        self.set_password(password)  # Устанавливаем хешированный пароль
        self.save()

        self.send_welcome_email(password)  # Отправляем email пользователю

    def send_welcome_email(self, password):
        """Отправляет email пользователю с данными для входа"""
        if not self.email:
            return  # Если email нет, не отправляем письмо

        subject = 'Добро пожаловать в нашу систему!'
        message = f'''
        Привет, {self.username}! 👋

        Мы рады приветствовать вас в нашей системе! 🎉

        Ваши данные для входа:
        🔑 Логин: {self.username}
        🔐 Пароль: {password}

        ⚠️ Не передавайте эти данные третьим лицам!

        Если возникнут вопросы, мы всегда на связи. 🤝

        С уважением,  
        Команда ClubOfProgg 🚀
        '''
        send_mail(subject, message, 'duishobaevislam01@gmail.com', [self.email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
