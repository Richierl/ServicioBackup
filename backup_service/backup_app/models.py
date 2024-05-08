from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Backup(models.Model):
    backup_name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='backups/')
    size_in_mb = models.PositiveIntegerField(default=0)  # Valor por defecto

    def __str__(self):
        return self.backup_name