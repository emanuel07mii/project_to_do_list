from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.CharField(max_length=50)
    concluido = models.BooleanField(default=False)
    arquivada = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    data_arquivamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tarefa