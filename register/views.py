from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, MyPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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

        if request.method == 'POST':

            form = MyPasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('reset_sucesso')
            else:
                context = {'form': form}
                return render(request, 'reset_pass.html', context)
        
        form = MyPasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'reset_pass.html', context)
    else:
        return redirect('index')

def reset_sucesso(request):
    if request.user.is_authenticated:
        response = render(request, 'reset_sucesso.html')
    else:
        response = redirect('index')
    
    return response