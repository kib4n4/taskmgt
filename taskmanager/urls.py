#taskmanager/urls.py

from django.urls import path, include
from .views import TaskViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
