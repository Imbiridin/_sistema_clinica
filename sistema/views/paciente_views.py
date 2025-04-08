from django.shortcuts import render

from sistema.models import Paciente

def listarPacientes(request):
    pacientes = Paciente.objects.all() # Váriavel paciente está guardando todos os objetos da tabela Paciente.

    context = { # Declaração de um dicionário que possui a chave pacientes e o valor pacientes(variável criada acima).
        'pacientes': pacientes,
    }

    return render(
        request,
        'paciente/listar.html',
        context,
    )