from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request='home.html')


def contexto(request):
    context = {
        'nome': 'João',
        'idade': 30,
        'hobbies': ['Leitura', 'Ciclismo', 'Cozinhar']
    }   
    return render(request, 'contexto.html', context)
