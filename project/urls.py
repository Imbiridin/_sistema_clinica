# São as importações realizadas de forma a utilizar parte do django.
from django.contrib import admin
from django.urls import path

# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('admin/', admin.site.urls),
]

# path() -> é um método do django que permite a inserção de uma url.
