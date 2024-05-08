# En forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Backup

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = ['backup_name', 'description', 'file']

    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            # Obtener la extensión del archivo
            file_extension = file.name.split('.')[-1].lower()
            # Validar que el archivo sea una imagen o un PDF
            allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'pdf']
            if file_extension not in allowed_extensions:
                raise ValidationError('Solo se permiten imágenes (JPG, JPEG, PNG, GIF) o archivos PDF.')
        return file
