from django.urls import path
from .views import *

app_name = 'sys_inventaire'

urlpatterns = [
    path('', index, name='index')
]