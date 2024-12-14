from django.db import models
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')  # Связь с проектом
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Поле описания может быть пустым
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Исполнитель задачи
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')  # Статус задачи
    due_date = models.DateTimeField(null=True, blank=True)  # Дата завершения задачи

    def __str__(self):
        return self.title
    
from django.utils import timezone

def create_tasks():
    tasks = [
        {'project_id': 4,'title':'Task A1','description':'Description for Task A1','assignee_id':1,'status':'new','due_date':timezone.now() + timezone.timedelta(days=7)},
        {'project_id': 5,'title':'Task A2','description':'Description for Task A2','assignee_id':2,'status':'new','due_date':timezone.now() + timezone.timedelta(days=14)},
        {'project_id': 6,'title':'Task B1','description':'Description for Task B1','assignee_id':3,'status':'in_progress','due_date':timezone.now() + timezone.timedelta(days=10)},
        {'project_id': 7,'title':'Task A1','description':'Description for Task A1','assignee_id':4,'status':'in_progress','due_date':timezone.now() + timezone.timedelta(days=10)},
        {'project_id': 8,'title':'Task B1','description':'Description for Task B1','assignee_id':2,'status':'in_progress','due_date':timezone.now() + timezone.timedelta(days=10)},
        {'project_id': 9,'title':'Task C2','description':'Description for Task C2','assignee_id':6,'status':'in_progress','due_date':timezone.now() + timezone.timedelta(days=10)},
        {'project_id': 10,'title':'Task C1','description':'Description for Task C1','assignee_id':5,'status':'in_progress','due_date':timezone.now() + timezone.timedelta(days=10)},
        # Добавьте остальные задачи...
    ]

    for task_data in tasks:
        Task.objects.create(**task_data)

# create_tasks()
