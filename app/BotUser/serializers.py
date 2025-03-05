from rest_framework import serializers
from .models import BotUser

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ["id", "telegram_id", "name", "username", "is_admin"]
