from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'inventory.html')

def montrer_medicament(request):
    items = Medicament.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'inventory.html', context)