from django.urls import path
from .views import *

app_name = 'sys_inventaire'

urlpatterns = [
    path('', index, name='index'), 
    path('medicaments/', montrer_medicament, name='medicament'),
    path('paraphamacies/', montrer_parapharmacie, name='paraphamacies'),
    path('dietetiques/', montrer_dietetique, name='dietetiques'),
    path('pti_materiel/', montrer_petit_materiel, name='pti_materiel'), 
    # les ajouts de nouveaux produits
    path('ajoutMedicament/', ajout_medicament, name='ajouter_medicament'),
    path('ajoutpara/', ajout_parapharmacie, name='ajouter_parapharmacie'),
    path('ajoutPetitMaretiel/', ajout_petit_materiel, name='ajouter_petit_materiel'),
    path('ajoutDietetique/', ajout_dietetique, name='ajouter_dietetique'),
]