from rest_framework import serializers

from todo.models import Todo, TodoList


class TodoSerialiser(serializers.ModelSerializer):
    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Todo
        exclude = ['due_date']


class TodoListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
