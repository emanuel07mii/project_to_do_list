from django import forms

class TarefaForm(forms.Form):
    '''Formulario Para Tarefas'''
    tarefa = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_tarefa',
                'class': 'form-control',
                'placeholder': 'Digite sua tarefa...',
            }
        )
        )
