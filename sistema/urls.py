from django.urls import path
# Importação do módulo views.py, onde tem a view index
from sistema import views

app_name = 'sistema'


urlpatterns = [
    path('', views.index, name='index'),
    path('marcos/', views.marcos),
]
