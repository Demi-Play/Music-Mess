from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('producer', 'Продюсер'),
        ('musician', 'Музыкант'),
        ('vocalist', 'Вокалист'),
    ]

    id = models.AutoField(primary_key=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50)
    profile_settings = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}, {self.email}, {self.role}"