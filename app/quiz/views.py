from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Topic, Question
from .serializers import TopicSerializer, QuestionSerializer


class TopicViewSet(ModelViewSet):
    """ViewSet для тем"""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Автоматически устанавливает текущего пользователя как создателя темы"""
        serializer.save(create_user=self.request.user)


class QuestionViewSet(ModelViewSet):
    """ViewSet для вопросов"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Автоматически устанавливает текущего пользователя как создателя вопроса"""
        serializer.save(create_user=self.request.user)
