from django.http import JsonResponse


# Create your views here.


def adicionar(request, id):
    carrinho = request.session.get('carrinho', [])
    if isinstance(carrinho, list):
        carrinho.append(id)
        request.session['carrinho'] = carrinho
    else:
        request.session['carrinho'] = [id]

    return JsonResponse({
        "mensagem": "item adicionado ao carrinho"
    })