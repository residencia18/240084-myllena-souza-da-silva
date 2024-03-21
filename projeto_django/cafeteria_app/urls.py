from django.urls import path
from cafeteria_app import views

urlpatterns = [
    path("", views.home),
]