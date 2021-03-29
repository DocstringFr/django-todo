from django.contrib import admin
from django.urls import path

from todo.views import TodosListView, CreateTodo, update_todo, DeleteTodo, delete_all

urlpatterns = [
    path('', TodosListView.as_view(), name='home'),
    path('create/', CreateTodo.as_view(), name='create-todo'),
    path('update/<int:pk>/', update_todo, name='update-todo'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete-todo'),
    path('delete_all/', delete_all, name='delete-all-todo'),
    path('admin/', admin.site.urls),
]
