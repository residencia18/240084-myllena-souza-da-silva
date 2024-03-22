from django.db import models

# Create your models here.

class Produto (models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    codigo = models.IntegerField() #validators = [MinValueValidator(2),  MaxValueValidator(5)])
    def __str__ (self):
        return self.nome
    
