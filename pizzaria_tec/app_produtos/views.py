from django.shortcuts import render, redirect
from .models import Produto, Compra, CompraProduto
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'app_produtos/globals/home.html', {"produtos":produtos})

@login_required(login_url='/login/login')
@permission_required('app_produtos.add_produto', raise_exception=False, login_url="/error/404/")
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

def carrinho(request):
    carrinho = request.session.get('carrinho', [])
    return render(request, 'app_produtos/globals/carrinho.html', {"carrinho":carrinho})

def finalizar_compra(request):
    carrinho = request.session.get('carrinho', [])
    compra = Compra.objects.create()
    for id in carrinho:
        CompraProduto.objects.create(compra_id=compra, produto_id=Produto.objects.get(id=id))
    request.session['carrinho'] = []
    return redirect('carrinho')


def vizualizar(request):
    vendas = CompraProduto.objects.select_related('compra_id', 'produto_id').all()
    for i in vendas:
        print(i.produto_id.preco)
    import ipdb; ipdb.set_trace()
    return render(request, 'app_produtos/globals/vizualizar.html', {"vendas":vendas})