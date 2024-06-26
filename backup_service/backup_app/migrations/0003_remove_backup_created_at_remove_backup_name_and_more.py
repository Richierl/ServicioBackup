# Generated by Django 5.0.3 on 2024-05-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup_app', '0002_remove_backup_data_remove_backup_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backup',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='backup',
            name='name',
        ),
        migrations.AddField(
            model_name='backup',
            name='file',
            field=models.FileField(default='default_file.txt', upload_to='backups/'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='size_in_mb',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
