from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()
    img = models.CharField(max_length=100)

    def __str__(self):

        return "Produto: {}, Preço: {}, Imagem: {}".format(self.nome_produto, self.preco, self.img)
