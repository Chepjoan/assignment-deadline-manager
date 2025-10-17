from django.db import models
from django.contrib.auth.models import User

class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_assignments = models.IntegerField(default=0)
    completed_assignments = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Progress"
