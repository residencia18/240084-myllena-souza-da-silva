from django.urls import path, include
from comida_app import views

# criando as rotas para aonde a pagina vai ser redirecionada
urlpatterns = [
    path('', views.home, name= 'home'),
    path('sobre/', views.sobre, name= 'sobre'),
    path('breakfast/', views.breakfast, name= 'breakfast'),
]
