from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app_produtos.views import index

# Create your views here.
def login_request(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        message = "Usuário ou senha inválidos"
    return render(request, 'login.html', {"message":message})

def logout_request(request):
    logout(request)
    return redirect(login_request)

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            User.objects.create_user(username=username, email=email, password=password)
        return render(request, 'login.html')
    return render(request, 'cadastrar.html')

