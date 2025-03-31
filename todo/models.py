from django.db import models
from private_storage.fields import PrivateFileField


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='public', null=True)
    private_file = PrivateFileField(upload_to='private', null=True)
    list = models.ForeignKey('TodoList', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'


class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
