from django.db import models
from files.models import File
from django.contrib.auth import get_user_model

User = get_user_model()

class AudioComment(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} at {self.timestamp}"