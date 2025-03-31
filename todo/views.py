from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo, TodoList
from todo.serializers import TodoSerialiser, TodoListSerialiser


# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiser
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('due_date', 'completed', 'favourite')
    search_fields = ('title',)
    pagination_class = CustomPageNumberPagination


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerialiser
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
