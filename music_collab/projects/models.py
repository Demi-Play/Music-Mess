from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В работе'),
        ('completed', 'Завершен'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    # sequencer_data = models.JSONField(default=dict, blank=True)  # Для хранения данных секвенсора

    def __str__(self):
        return self.name


class AudioMaterial(models.Model):
    project = models.ForeignKey(Project, related_name='audio_materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class JoinRequest(models.Model):
    project = models.ForeignKey(Project, related_name='join_requests', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} requests to join {self.project.name}"
    
