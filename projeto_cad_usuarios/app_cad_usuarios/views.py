from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):

    # Salvar as informações da tela para o banco de dados
    novo_usuarios = Usuario()
    novo_usuarios.nome = request.POST.get('nome')
    novo_usuarios.nome = request.POST.get('idade')

    # Exibir todod os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
