from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import Tarefa
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.utils import timezone

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
                if tarefa.concluido == True and tarefa.arquivada == False:
                    tarefas_concluidas.append(tarefa)
                else:
                    if tarefa.arquivada == False:
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
                    tarefa.data_conclusao = timezone.now()
                    tarefa.save()
        
        return redirect('index')
    else:
        return redirect('index')

def excluir(request, id):

    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user=request.user)
        
        if tarefas_total is not None:
            for tarefa in tarefas_total:
                if tarefa.id == id and tarefa.arquivada == True:
                    tarefa.delete()
                    return redirect('tarefas_arquivadas')
                elif tarefa.id == id:
                    tarefa.delete()
        return redirect('index')
    else:
        return redirect('index')

def arquivar_tarefa(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        if tarefa is not None:
            tarefa.arquivada = True
            tarefa.data_arquivamento = timezone.now()
            tarefa.save()
    return redirect('index')

def tarefas_arquivadas(request):
    if request.user.is_authenticated:
        tarefas = Tarefa.objects.filter(user=request.user, arquivada=True)
        return render(request, 'to_do_lists/arquivadas.html', {'tarefas': tarefas})
    else:
        return render(request, 'to_do_lists/index.html')
