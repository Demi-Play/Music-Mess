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
    

def create_projects():
    projects = [
        {'name': "Project Alpha", 'description' : "First project description", 'owner_id' : 1, 'status' : "in_progress"},
        {'name' : "Project Beta", 'description' : "Second project description", 'owner_id' : 2, 'status' : "in_progress"},
        {'name' : "Project Gamma", 'description' : "Third project description", 'owner_id' : 3, 'status' : "completed"},
        {'name' : "Project Delta", 'description' : "Fourth project description", 'owner_id' : 4, 'status' : "in_progress"},
        {'name' : "Project Epsilon", 'description' : "Fifth project description", 'owner_id' : 5, 'status' : "completed"},
    ]

    for project_data in projects:
        Project.objects.create(**project_data)

# create_projects()


def create_audio_materials():
    audio_materials = [
        {'project_id':3,'title':'Audio Track A1','audio_file':'audio/lazarus.mp3'},
        {'project_id':4,'title':'Audio Track A2','audio_file':'audio/was_hatneen.mp3'},
        # Добавьте остальные аудиоматериалы...
    ]

    for audio_material_data in audio_materials:
        AudioMaterial.objects.create(**audio_material_data)

# create_audio_materials()

