# Generated by Django 5.1.7 on 2025-03-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_options_alter_todolist_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='attachment',
            field=models.FileField(null=True, upload_to='public'),
        ),
    ]
