from django.contrib import admin

# Impportação do módulo models.py
from sistema import models


# Aqui fica  registro do model do Paciente.
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)


@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    search_fields = ('ativo',)


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'crm', 'especialidade', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'crm',)