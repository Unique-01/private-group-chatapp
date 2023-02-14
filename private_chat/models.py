from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=500)
    centent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room
