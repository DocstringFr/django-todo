"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
