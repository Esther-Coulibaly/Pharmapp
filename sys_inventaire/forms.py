from  django import forms
from .models import *

class Petit_matérielForm(forms.ModelForm):
    class Meta:
        model = Petit_matériel
        fields = ('nom_article', 'quantite', 'prix', 'date_peremption', 'Numero_lot')

class ParapharmatieForm(forms.ModelForm):
    class Meta: 
        model = Parapharmatie
        fields = ('nom_article', 'quantite', 'prix', 'date_peremption', 'Numero_lot')

class DietetiqueForm(forms.ModelForm):
    class Meta: 
        model = Dietetique
        fields = ('nom_article', 'quantite', 'prix', 'date_peremption', 'Numero_lot')

class MedicamentForm(forms.ModelForm):
    class Meta:
        model =  Medicament
        fields = ('groupe', 'dci', 'specialite', 'dose', 'quantite', 'classe_therapeutic', 'prix', 'presentation', 'date_peremption', 'Numero_lot')