from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        response = redirect('index')
    else:
        response = render(request, 'register.html')
    
    return response

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