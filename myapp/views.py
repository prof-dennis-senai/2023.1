from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/globals/home.html')

def sobre(request):
    return render(request, 'myapp/globals/sobre.html')

def contato(request):
    return render(request, 'myapp/globals/contato.html')