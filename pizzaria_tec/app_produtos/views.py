from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'app_produtos/globals/home.html', {"produtos":produtos})

def adicionar(request):
    produto = {}
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        preco = request.POST.get('preco')
        img = request.POST.get('img')
        if nome_produto and preco and img:
            produto = {
                "nome_produto": nome_produto,
                "preco": preco,
                "img": img
            }

            Produto.objects.create(**produto)

    return render(request, 'app_produtos/globals/adicionar.html', {"produto":produto})
