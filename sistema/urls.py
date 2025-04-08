# São as importações realizadas de forma a utilizar partes do django
from django.urls import path
# Importação do diretório views.py, onde tem a view index e a view listarPacientes.
from sistema import views

app_name = 'sistema'


urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listarPacientes, name= 'listar'),
    path('listarmedicos/', views.listarMedicos, name= 'listar'),
]
