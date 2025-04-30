from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.CharField(max_length=50)
    concluido = models.BooleanField(default=False)
    arquivada = models.BooleanField(default=False)

    def __str__(self):
        return self.tarefa