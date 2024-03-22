from django.db import models

class Backup(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'backup_app'  # Agregar app_label para la clase Backup
# Create your models here.
