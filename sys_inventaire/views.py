from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
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
        'items': items,
        'titre': 'Parapharmacie'
    }
    return render(request, 'inventory.html', context)

def montrer_petit_materiel(request):
    items = Petit_matériel.objects.all()
    context = {
        'items': items,
        'titre': 'Petit matériel'
    }
    return render(request, 'inventory.html', context)

def montrer_dietetique(request):
    items = Dietetique.objects.all()
    context = {
        'items': items,
        'titre': 'Diétitique'
    }
    return render(request, 'inventory.html', context)

def ajouter_produit(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sys_inventaire:index')
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

def modifier_article(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    
    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('sys_inventaire:index')
    else:
        form = cls(instance=item)
        return render(request, 'modifpage.html', {'form':form})

def modifier_medicament(request, pk):
    return modifier_article(request, pk, Medicament, MedicamentForm)


def modifier_dietetique(request, pk):
    return modifier_article(request, pk, Dietetique, DietetiqueForm)

def modifier_parapharmacie(request, pk):
    return modifier_article(request, pk, Parapharmatie, ParapharmatieForm)


def modifier_petit_materiel(request, pk):
    return modifier_article(request, pk, Petit_matériel, Petit_matérielForm)


def supprimer_medicament(request, pk):
    Medicament.objects.filter(id=pk).delete()
    items = Medicament.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def supprimer_medicament(request, pk):
    Medicament.objects.filter(id=pk).delete()
    items = Medicament.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def supprimer_parapharmatie(request, pk):
    Parapharmatie.objects.filter(id=pk).delete()
    items = Parapharmatie.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def supprimer_dietetique(request, pk):
    Dietetique.objects.filter(id=pk).delete()
    items = Dietetique.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)

def supprimer_petit_matériel(request, pk):
    Petit_matériel.objects.filter(id=pk).delete()
    items = Petit_matériel.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inventory.html', context)