# Generated by Django 4.2.5 on 2024-09-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.CharField(default='text', max_length=20),
        ),
    ]
