# Generated by Django 4.1.5 on 2023-01-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0006_userprofilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='image',
            field=models.ImageField(upload_to='capp/static'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='resume',
            field=models.FileField(upload_to='capp/static'),
        ),
    ]
