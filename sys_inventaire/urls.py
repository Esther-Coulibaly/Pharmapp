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
    path('ajoutPetitMateriel/', ajout_petit_materiel, name='ajouter_petit_materiel'),
    path('ajoutDietetique/', ajout_dietetique, name='ajouter_dietetique'),

    # La modification particuliere d'articles enregistré en cas d'erreur
    path('modifierMedicament/<int:pk>/', modifier_medicament, name='modifier_medicament'),
    path('modifierpar/<int:pk>', modifier_parapharmacie, name='modifier_parapharmacie'),
    path('modifierpetitmateriel/<int:pk>/', modifier_petit_materiel, name='modifier_petit_materiel'),
    path('modifierdietetique/<int:pk>/', modifier_dietetique, name='modifier_dietetique'),
    
    # La suppression particuliere des articles 
    path('supprimerMedicament/<int:pk>/', supprimer_medicament, name='supprimer_medicament'),
    path('supprimerParapharmatie/<int:pk>/', supprimer_parapharmatie, name='supprimer_parapharmatie'),
    path('supprimerDietetique/<int:pk>/', supprimer_dietetique, name='supprimer_dietetique'),
    path('supprimerPetitmatieriel/<int:pk>/', supprimer_petit_matériel, name='supprimer_petit_matériel')
]