from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from tarefas.models import Tarefa

# Views usando o django.views.generic

class TodoListView(ListView):
    model = Tarefa

# View para criação de novas tarefas
class TodoCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_final'] # Campos que serão carregados
    success_url = reverse_lazy('todo_list') # Retorna para pagina "todo_list"

# View para editar tarefas existentes
class TodoUpdateView(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_final']
    success_url = reverse_lazy('todo_list')

# View para deletar tarefas existentes
class TodoDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('todo_list')

