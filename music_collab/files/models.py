from django.db import models
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):
    FILE_TYPE_CHOICES = [
        ('audio', 'Аудио'),
        ('midi', 'MIDI'),
        ('preset', 'Пресет'),
    ]
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='uploads/')  # Файлы будут сохраняться в media/uploads/
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name, self.uploaded_by, self.file_type, self.uploaded_at