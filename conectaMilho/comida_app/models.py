from django.db import models

# Create your models here.

class Registro (models.Model):
    nome = models.CharField (max_length = 100)
    dataRegist = models.DateField (auto_now_add = True)
    precoProduto = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nome
    