from django.urls import path
from lojaMiniaturas_app import views


urlpatterns = [
    path('', views.home),
]
