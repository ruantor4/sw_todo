from django.contrib.auth.models import User
from django.db import models

# Status estáticos definidos pelo sistema
STATUS_CHOICES = [
    ('PENDENTE', 'Pendente' ), # 'BANCO', 'APRESENTAÇÃO'
    ('CONCLUIDA', 'Concluída' ),
    ('ATRASADA', 'Atrasada' ),
]

# Create your models here.
class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # usuário da tarefa
    titulo = models.CharField(max_length=100, null=False, blank=False) # Maximo 100 caracteres nao pode ser nulo nem branco.
    descricao = models.TextField(null=True, blank=True) # Pode ser nulo e branco (opcional)
    data_criacao = models.DateTimeField(auto_now_add=True) # Data registrada automaticamente pelo sistema na criação.
    status = models.CharField(choices=STATUS_CHOICES, default='PENDENTE', max_length=10) # Usando "choices" para escolha do status
    data_final = models.DateTimeField(null=False, blank=False) # Data final da tarefa, nao pode ser nulo ou branco.

    class Meta:
        db_table = 'tarefas' # Nomeia a tabela
        ordering = ['data_final', 'data_criacao'] # Ordena as consultas no banco por data_final, depois data_criacao
