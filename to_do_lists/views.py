from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa
from django.http import HttpResponse
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
        
        if request.method == 'POST':
            form = TarefaForm(request.POST)

            if form.is_valid():
                user = request.user
                tarefa = form.cleaned_data['tarefa']
                concluido = False
                new_tarefa = Tarefa.objects.create(user=user, tarefa=tarefa, concluido=concluido)
                new_tarefa.save()

                return redirect('index')
            else:
                context = {'form':form,
                            'tarefas_concluidas': tarefas_concluidas,
                            'tarefas_nao_concluidas': tarefas_nao_concluidas,
                        }
                response = render(request, 'to_do_lists/index.html', context)
                return response
        else:
            form = TarefaForm()
            context = {'form':form,
                        'tarefas_concluidas': tarefas_concluidas,
                        'tarefas_nao_concluidas': tarefas_nao_concluidas,
                    }
            return render(request, 'to_do_lists/index.html', context)
    else:
        return response

def concluir(request, id):

    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user=request.user)
        
        if tarefas_total is not None:

            for tarefa in tarefas_total:
                if tarefa.id == id:
                    tarefa.concluido = True
                    tarefa.save()
        
        return redirect('index')
    else:
        return redirect('index')

def excluir(request, id):

    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user=request.user)
        
        if tarefas_total is not None:
            for tarefa in tarefas_total:
                if tarefa.id == id:
                    tarefa.delete()

        return redirect('index')
    else:
        return redirect('index')