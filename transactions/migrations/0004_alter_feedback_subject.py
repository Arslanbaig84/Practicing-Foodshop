# Generated by Django 4.2.5 on 2024-09-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_feedback_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=20),
        ),
    ]
