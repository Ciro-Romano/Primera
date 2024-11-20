from django.shortcuts import render

def Inicio(request):
    return render(request, 'aplicacion/inicio.html')
