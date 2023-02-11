from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    participant = models.ManyToManyField(User,related_name='participant')
    admin = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admin')
    room_name=models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
    


class RoomMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}-{self.content:30}'

    
