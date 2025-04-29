from django.shortcuts import render

# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'global/base.html'
    )

def login(request):
    return render(
        request,
        'usuario/login.html'
    )

# REQUEST - RESPONSE - RENDER