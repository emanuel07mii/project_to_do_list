from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, MyPasswordChangeForm

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
        else:
            return render(request, 'register.html', {'form': form})
    
    form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})

def sucesso(request):
    if request.user.is_authenticated:
        response = redirect('index')
    else:
        response = render(request, 'sucesso.html')
    
    return response

def reset_pass(request):
    if request.user.is_authenticated:
        response = render(request, 'reset_pass.html')
    else:
        response = redirect('index')
    
    return response

def reset_sucesso(request):
    if request.user.is_authenticated:
        response = render(request, 'reset_sucesso.html')
    else:
        response = redirect('index')
    
    return response