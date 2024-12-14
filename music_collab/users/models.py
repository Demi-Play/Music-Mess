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
    
# from django.utils import timezone

# def create_users():
#     users = [
#         {'username': 'producer1', 'password_hash': 'hashed_password1', 'role': 'producer', 'email': 'producer1@example.com', 'status': 'active'},
#         {'username': 'musician1', 'password_hash': 'hashed_password2', 'role': 'musician', 'email': 'musician1@example.com', 'status': 'active'},
#         {'username': 'vocalist1', 'password_hash': 'hashed_password3', 'role': 'vocalist', 'email': 'vocalist1@example.com', 'status': 'active'},
#         {'username': 'producer2', 'password_hash': 'hashed_password4', 'role': 'producer', 'email': 'producer2@example.com', 'status': 'active'},
#         {'username': 'musician2', 'password_hash': 'hashed_password5', 'role': 'musician', 'email': 'musician2@example.com', 'status': 'active'},
#         {'username': 'vocalist2', 'password_hash': 'hashed_password6', 'role': 'vocalist', 'email': 'vocalist2@example.com', 'status': 'active'},
#         {'username': 'producer3', 'password_hash': 'hashed_password7', 'role': 'producer', 'email': 'producer3@example.com', 'status': 'active'},
#         {'username': 'musician3', 'password_hash': 'hashed_password8', 'role': 'musician', 'email': 'musician3@example.com',  'status':'active'},
#         {'username': 'vocalist3','password_hash':'hashed_password9','role':'vocalist','email':'vocalist3@example.com','status':'active'},
#         {'username':'producer4','password_hash':'hashed_password10','role':'producer','email':'producer4@example.com','status':'active'},
#     ]

#     for user_data in users:
#         user = CustomUser(**user_data)
#         user.set_password(user_data['password_hash'])  # Убедитесь, что вы используете метод для установки пароля
#         user.save()

# create_users()