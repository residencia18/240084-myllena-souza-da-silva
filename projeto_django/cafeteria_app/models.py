from django.db import models

# Create your models here.
#criando tabela no banco de dados
class Bebida(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    data_registro = models.DateTimeField(auto_now_add = True)
    def __str__ (self):
        #retornar apena ao nome da bebida
        return  self.nome