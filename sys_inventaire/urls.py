from django.urls import path
from .views import *

app_name = 'sys_inventaire'

urlpatterns = [
    path('', index, name='index'), 
    path('medicaments/', montrer_medicament, name='medicament'),
    path('paraphamacies/', montrer_parapharmacie, name='paraphamacies'),
    path('dietetiques/', montrer_dietetique, name='dietetiques'),
    path('pti_materiel/', montrer_petit_materiel, name='pti_materiel')
]