from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.http import JsonResponse
from app_produtos.models import Produto
from django.views import View
import json



# @csrf_exempt
# def criar_produto(request: HttpRequest):
#     if request.method == 'POST':
#         itens = json.loads(request.body)
#         nome_produto = itens.get('nome_produto')
#         preco = itens.get('preco')
#         img = itens.get('img')
#         if nome_produto and preco and img:
#             Produto.objects.create(
#                 nome_produto=nome_produto,
#                 preco=preco,
#                 img=img
#             )

#         return JsonResponse({
#             "mensagem": "item criado com sucesso"
#         }, status=201)

#     else:
#         produtos = Produto.objects.all()
#         return JsonResponse(list(produtos.values()), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class ProdutoView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return JsonResponse(list(produtos.values()), safe=False)
    