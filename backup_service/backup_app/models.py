from django.db import models
from django.utils import timezone
from datetime import datetime

class Backup(models.Model):
    name = models.CharField(max_length=255)
    size_in_mb = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # o default=datetime.now si no usas django.utils.timezone

    def __str__(self):
        return self.name
