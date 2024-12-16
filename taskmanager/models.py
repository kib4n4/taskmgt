from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    deleted = models.BooleanField(default=False) #soft delete

    def __str__(self):
        return self.name
    def Soft_delete(self):
        self.deleted = True
        self.save()

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False) #soft delete
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    
    def __str__(self):
        return self.title
    
    def Soft_delete(self):
        self.deleted = True
        self.save()