from django.shortcuts import render

# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'global/base.html'
    )

def marcos(request):
    return render(
        request,
        'global/marcos.html'
    )

# REQUEST - RESPONSE - RENDER