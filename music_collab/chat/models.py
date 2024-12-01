from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat for {self.project.name} created at {self.created_at}"

class Message(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('text', 'Текст'),
        ('video_call', 'Видеозвонок'),
        ('call', 'Звонок'),
        # Другие типы сообщений могут быть добавлены здесь.
    ]

    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на пользователя
    content = models.TextField()
    message_type = models.CharField(max_length=50, choices=MESSAGE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in chat {self.chat.id}"