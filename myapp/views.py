from django.shortcuts import render

data = [
    {"nome": "Joaquim"},
]
# Create your views here.
def home(request):
    nome = request.POST.get('nome')
    if nome:
        data.append({"nome": nome}) 
    return render(request, 'myapp/globals/home.html',{"dados":data,"ultimo_nome":nome},status=500)

def sobre(request):
    return render(request, 'myapp/globals/sobre.html')

def contato(request):
    return render(request, 'myapp/globals/contato.html')


def usuarios(request,id=None):
    try:
        nome = data[id-1]
    except:
        nome = None
    return render(request, 'myapp/globals/usuarios.html',nome)