from django.shortcuts import render

def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Gato(request):
    return render(request, 'aplicacion/gato.html')
