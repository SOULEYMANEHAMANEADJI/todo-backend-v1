from datetime import datetime

from django.test import TestCase

from todo.models import Todo, TodoList


# Create your tests here.
class TodoTestCase(TestCase):
    DUMMY_TODO_TITLE = 'Faire une pause'

    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name = 'Test Todo List'
        self.todoList.save()

        self.todoListTestElement = Todo()
        self.todoListTestElement.title = self.DUMMY_TODO_TITLE
        self.todoListTestElement.due_date = datetime.today()
        self.todoListTestElement.favourite = False
        self.todoListTestElement.completed = True
        self.todoListTestElement.list = self.todoList
        self.todoListTestElement.save()

    def test_create_todo(self):
        nb_of_todos_before_add = Todo.objects.count()
        new_todo = Todo()
        new_todo.title = 'Acheter de l\'eau'
        new_todo.due_date = datetime.today()
        new_todo.favourite = True
        new_todo.list = self.todoList
        new_todo.save()
        nb_of_todos_after_add = Todo.objects.count()
        self.assertTrue(nb_of_todos_after_add == nb_of_todos_before_add + 1)

    def test_update_todo(self):
        self.assertEqual(self.todoListTestElement.title, self.DUMMY_TODO_TITLE)
        self.todoListTestElement.title = 'Faire un repas'
        self.todoListTestElement.save()
        tmpElement = Todo.objects.get(pk=self.todoListTestElement.pk)
        self.assertEqual(tmpElement.title, 'Faire un repas')

    def test_delete_todo(self):
        nb_of_todos_before_delete = Todo.objects.count()
        self.todoListTestElement.delete()
        nb_of_todos_after_delete = Todo.objects.count()
        self.assertTrue(nb_of_todos_after_delete == nb_of_todos_before_delete - 1)