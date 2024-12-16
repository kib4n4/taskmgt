#taskmanager/views.py
from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
   # permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)
#Create new task
class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
  #  permission_classes = [IsAuthenticated]
#Read all tasks
class ListTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]

#Read a single task
class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]

#Update a task
class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
  #  permission_classes = [IsAuthenticated]

#Delete a task
class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
   # permission_classes = [IsAuthenticated]