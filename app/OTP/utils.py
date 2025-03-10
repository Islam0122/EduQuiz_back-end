# utils.py
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP
import random
import string

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(user_email):
    otp_code = generate_otp()
    OTP.objects.update_or_create(
        email=user_email,
        defaults={'code': otp_code}
    )

    subject = 'Ваш OTP код для подтверждения email'
    message = f"Ваш OTP код для подтверждения email: {otp_code}"
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )

