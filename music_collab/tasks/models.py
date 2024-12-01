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