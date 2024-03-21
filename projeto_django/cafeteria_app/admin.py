from django.contrib import admin
#importando classe bebida do app
from cafeteria_app.models import Bebida

# Register your models here.

#registrando a class bebidas
admin.site.register(Bebida)
