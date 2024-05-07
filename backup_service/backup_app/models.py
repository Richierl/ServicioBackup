from django.db import models
from django.utils import timezone
from datetime import datetime

class Backup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    backup_file = models.FileField(upload_to='backups/')

    def __str__(self):
        return self.name