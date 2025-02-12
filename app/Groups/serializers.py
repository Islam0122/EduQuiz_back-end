from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'is_active','group', 'created_at', 'updated_at', 'create_user')
        read_only_fields = ('created_at', 'updated_at', 'create_user')

    def create(self, validated_data):
        # Логика создания нового студента, если нужна дополнительная обработка
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Логика обновления студента, если требуется дополнительная обработка
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance


class StudentInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'full_name','group','is_active', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class GroupSerializer(serializers.ModelSerializer):
    students = StudentInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'created_at', 'updated_at', 'create_user', 'students')
        read_only_fields = ('created_at', 'updated_at', 'create_user')

    def create(self, validated_data):
        # Логика создания новой группы
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Логика обновления группы
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
