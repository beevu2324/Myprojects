# Generated by Django 5.0.1 on 2024-02-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
