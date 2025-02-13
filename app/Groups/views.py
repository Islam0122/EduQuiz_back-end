from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(create_user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = Group.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(create_user=user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(create_user=self.request.user)
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response
    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()
        return super().retrieve(request, *args, **kwargs)

