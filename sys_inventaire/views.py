from django.shortcuts import render, redirect
from .models import *
from .forms import *


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

def ajouter_produit(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            redirect('sys_inventaire:index')
    else:
        form = cls()
        return render(request, 'ajout_produit.html', {'form': form})

def ajout_medicament(request):
    return ajouter_produit(request, MedicamentForm)

def ajout_petit_materiel(request):
    return ajouter_produit(request, Petit_matérielForm)

def ajout_parapharmacie(request):
    return ajouter_produit(request, ParapharmatieForm)

def ajout_dietetique(request):
    return ajouter_produit(request, DietetiqueForm)