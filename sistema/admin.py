from django.contrib import admin

# Impportação do módulo models.py
from sistema import models


# Aqui fica  registro do model do Paciente.
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)

# Aqui fica o registro do model da Especialidade
@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    search_fields = ('ativo',)

# Aqui fica o registro do model do Medico
@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'crm', 'especialidade', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'crm',)

# Aqui fica o registro do model da Consulta
@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','medico_id', 'paciente_id','status',)
    search_fields = ('id', 'medico', 'paciente', 'horario','status')