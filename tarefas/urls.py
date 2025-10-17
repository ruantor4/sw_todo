"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

from tarefas import views
from tarefas.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [

    # Rota para listar todas tarefas na pagina inicial
    path('', TodoListView.as_view(), name="todo_list"),

    # Rota para criar novas tarefas
    path('create', TodoCreateView.as_view(), name="todo_create"),

    # Rota para editar usuario passando o ID
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),

    # Rota para deletar usuario passando o ID
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),

]
