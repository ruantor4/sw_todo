from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tarefas.models import Tarefa


# Create your views here.

class TodoListView(ListView):
    model = Tarefa


class TodoCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_final']
    success_url = reverse_lazy('todo_list')