from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()
    img = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ("add_produtos", "Pode adicionar produtos"),
        )

    def __str__(self):

        return "Produto: {}, Preço: {}, Imagem: {}".format(self.nome_produto, self.preco, self.img)


class Compra(models.Model):
    data_venda = models.DateField(auto_now=True)

    def __str__(self):

        return "Compra: {}, Preço: {}, Imagem: {}".format(self.data_venda)


class CompraProduto(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    compra_id = models.ForeignKey(Compra, on_delete=models.CASCADE)