from django.shortcuts import render, redirect
from sistema.forms import PacienteForm
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


# View referente a criação dos Pacientes
def criarPaciente(request):
    # Verificar se a requisição é do tipo POST
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados enviados.
        form = PacienteForm(request.POST, request.FILES)
        # POST -> Contém os campos do form (nome, email, etc...)
        # FILES -> Contém o arquivo enviados (imagens)
        if form.is_valid():
            # Se os dados forem válidos, é salvo um novo paciente no BD.
            form.save()
            return redirect( '/pacientes')
    else:
        # Se uma requisição for do tipo GET, exibe um formulário vazio
        form = PacienteForm()

    return render(
        request,
        'paciente/cadastro.html',
        {'form': form}    
    )
