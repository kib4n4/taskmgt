#taskmanager/serializers.py

from rest_framework import serializers
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    assignee = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
    def Validate_due_date(self,value):
        if value is None:
            raise serializers.ValidationError("Due date is required")
        return value

