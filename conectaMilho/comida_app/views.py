from django.shortcuts import render
from comida_app.models import Registro
from comida_app.models import Menu


# NA VIEW É ONDE FAZ O ACCESSO DO BANCO DE DADOS
# Create your views here.
def home(request):
    registro = Registro.object.order_by('id') #orde_by pega todos os registros
    context = {"registro" : registro}
    return render(request, 'index.html')

def sobre (request):
    return render(request, 'sobre.html')

def breakfast(request):
    menu = Menu.objects.get(nome = 'breakfast')
    context = {'registro': menu}
    return render(request, 'breakfast.html', context)
