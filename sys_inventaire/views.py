from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'inventory.html')

def montrer_medicament(request):
    items = Medicament.objects.all()
    header = 'Medicament'
    context = {
        'header':header,
        'items': items
    }
    return render(request, 'inventory.html', context)

def montrer_parapharmacie(request):
    items = Parapharmatie.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def montrer_petit_materiel(request):
    items = Petit_matériel.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def montrer_dietetique(request):
    items = Dietetique.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)