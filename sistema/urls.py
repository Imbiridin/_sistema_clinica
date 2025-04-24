# São as importações realizadas de forma a utilizar partes do django
from django.urls import path
# Importação do diretório views.py, onde tem a view index e a view listarPacientes.
from sistema import views

app_name = 'sistema'


urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.listarPacientes, name= 'pacientes'),
    path('pacientes/novo/', views.criarPaciente, name= 'criarPaciente'),
    path('pacientes/perfil/<int:paciente_id>', views.perfilPaciente, name= 'perfil_paciente'),
    path('medicos/', views.listarMedicos, name= 'medicos'),
    path('medicos/novo/', views.criarMedico, name= 'criarMedico'),
]
