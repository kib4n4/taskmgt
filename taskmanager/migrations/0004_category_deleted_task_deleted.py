# Generated by Django 4.2.17 on 2024-12-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskmanager", "0003_alter_task_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]
