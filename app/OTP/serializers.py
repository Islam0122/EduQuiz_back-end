from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import OTP

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email', 'code']

    def validate_code(self, value):
        email = self.initial_data.get('email')
        otp_records = OTP.objects.filter(email=email).order_by('-created_at')
        if not otp_records.exists():
            raise ValidationError("OTP для данного email не найден.")

        otp = otp_records.first()
        if not otp.is_valid():
            raise ValidationError("OTP истек.")

        if otp.code != value:
            raise ValidationError("Неверный OTP код.")

        return value