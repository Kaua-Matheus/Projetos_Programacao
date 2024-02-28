from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # roba, view responsável, nome de referência

    # Página inicial
    path('', views.home, name='home'),

    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
