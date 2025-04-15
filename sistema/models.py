# Importação do módulo models que tras métodos do banco de dados.
from django.db import models

#Impotação do módulo TIMEZONE que traz datas e horários.
from django.utils import timezone

# Aqui fica o model do paciente

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m/', blank=True)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Aqui fica o model da especialidade    
class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'
    

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    crm = models.CharField(max_length=6)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)
    especialidade = models.ForeignKey(Especialidade, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    horario = models.DateTimeField()
    descricao = models.TextField(blank=True)
    confirmar =  models.BooleanField(default=True)
    status = models.CharField(default = 'A',
                    max_length = 1,
                    choices = (
                        ('A', 'AGENDADA'),
                        ('C', 'CANCELADA'),
                        ('M', 'CONFIRMADA'),                              
                        ('R', 'REALIZADA'),
                    )
                    )
# A -> AGENDADA
# C -> CANCELADA
# M -> CONFIRMADA
# R -> REALIZADA    
    def __str__(self):
        return f'Consulta {self.status} com sucesso.'