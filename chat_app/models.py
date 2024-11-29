from django.db import models

# Create your models here.

# model for the messages
class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.timestamp}: {self.content}'
    