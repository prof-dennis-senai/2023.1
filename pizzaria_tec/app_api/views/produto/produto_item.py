from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.http import JsonResponse
from app_produtos.models import Produto
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class ProdutoItenView(View):
    def get(self, request, id):
        try:
                
            produtos = Produto.objects.get(id=id)
            return JsonResponse({
                "id": produtos.id,
                "nome_produto": produtos.nome_produto,
                "preco": produtos.preco,
                "img": produtos.img 
            }, safe=False)
    
        except:
            return JsonResponse({
                "mensagem": "item não encontrado"
            }, status=404)
    
    def put(self, request, id):
        itens = json.loads(request.body)
        nome_produto = itens.get('nome_produto')
        preco = itens.get('preco')
        img = itens.get('img')
        item = Produto.objects.get(id=id)
        if nome_produto:    
            item.nome_produto = nome_produto
        if preco:            
            item.preco = preco
        if img:            
            item.img = img
        if nome_produto or preco or img:
            item.save()
            return JsonResponse({
                "mensagem": "item atualizado com sucesso"
            }, status=201)
        return JsonResponse({
            "mensagem": "nenhum dado alterado"
        })
    

    def delete(self, request, id):
        item = Produto.objects.get(id=id)
        item.delete()
        return JsonResponse({
            "mensagem": "item deletado com sucesso"
        }, status=201)
