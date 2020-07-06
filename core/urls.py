from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *



app_name = 'core'

urlpatterns = [
    path('', index, name='intro'),
    path('connexion/', LoginView.as_view(), name='connexion'),
    path('deconnexion/', LogoutView.as_view(), name='deconnexion'),
    path('enregistrer/', enregistrer_user, name='enregistrement'),
]