from django.db import models

class Backup(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
