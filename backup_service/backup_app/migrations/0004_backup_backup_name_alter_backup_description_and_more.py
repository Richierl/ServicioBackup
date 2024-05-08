# Generated by Django 5.0.3 on 2024-05-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup_app', '0003_remove_backup_created_at_remove_backup_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='backup_name',
            field=models.CharField(default='Default Backup Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='backup',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='backup',
            name='file',
            field=models.FileField(upload_to='backups/'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='size_in_mb',
            field=models.IntegerField(default=0),
        ),
    ]
