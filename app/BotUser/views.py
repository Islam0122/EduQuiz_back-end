from rest_framework.viewsets import ModelViewSet
from .models import BotUser
from .serializers import BotUserSerializer

class BotUserViewSet(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = "telegram_id"  # Поиск по Telegram ID вместо стандартного `id`
