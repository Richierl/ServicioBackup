# Generated by Django 5.0.3 on 2024-05-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup_app', '0004_backup_backup_name_alter_backup_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='backup_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='backup',
            name='description',
            field=models.TextField(),
        ),
    ]