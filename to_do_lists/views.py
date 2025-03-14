from django.shortcuts import render
from .forms import TarefaForm
from .models import Tarefa
# from django.http import HttpResponse
from django.views.decorators.cache import never_cache

@never_cache
def index(request):

    response = render(request, 'to_do_lists/index.html')
    
    if request.user.is_authenticated:
        # O trecho de código a seguir configura os cabeçalhos HTTP na resposta
        # para instruir o navegador a não armazenar a página em cache.
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        tarefas_total = Tarefa.objects.filter(user=request.user)
        if tarefas_total is not None:
            tarefas_concluidas = []
            tarefas_nao_concluidas = []

            for tarefa in tarefas_total:
                if tarefa.concluido == True:
                    tarefas_concluidas.append(tarefa)
                else:
                    tarefas_nao_concluidas.append(tarefa)
        else:
            tarefas_concluidas = None
            tarefas_nao_concluidas = None

        form = TarefaForm()
        context = {'form':form,
                   'tarefas_concluidas': tarefas_concluidas,
                   'tarefas_nao_concluidas': tarefas_nao_concluidas}
        response = render(request, 'to_do_lists/index.html', context)
    
    return response
