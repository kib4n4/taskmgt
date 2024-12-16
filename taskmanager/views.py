#taskmanager/views.py
from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import action 

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):#only show non-deleted tasks
        return Category.objects.filter(deleted=False)
    
    @action(detail=False, methods=['get'])
    def deleted(self,request):
        deleted_categories = Category.objects.filter(deleted=True)
        serializer = CategorySerializer(deleted_categories, many=True)
        return Response(serializer.data)


    def perform_destroy(self, instance):
        instance.soft_delete()#soft delete
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
   # permission_classes = [IsAuthenticated]

    def get_queryset(self):#only show non-deleted tasks
        return Task.objects.filter(deleted=False)
    
    @action(detail=False, methods=['get'])
    def deleted(self,request):
        deleted_tasks = Task.objects.filter(deleted=True)
        serializer = TaskSerializer(deleted_tasks, many=True)
        return Response(serializer.data)
    
    def perform_destroy(self, instance):
        instance.soft_delete()#soft delete

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