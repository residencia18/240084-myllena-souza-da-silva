from django.db import models

# Create your models here.

class Registro (models.Model):
    nome = models.CharField (max_length = 100)
    dataRegist = models.DateField (auto_now_add = True)
    precoProduto = models.DecimalField(max_digits=5, decimal_places=2)
    
    # criar chave estrangeira para relacionanar um banco de dados com o outro
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, null=True) #FireinKey significa chave estrangeira, on_delete=models.CASCADE apaga o 
    
    def __str__(self):
        return self.nome
    
class Menu (models.Model):
    nome = models.CharField (max_length = 50) # charfild tem limite de caractere
    
    def __str__ (self):
        return self.nome
    
