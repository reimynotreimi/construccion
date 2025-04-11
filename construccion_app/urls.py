# construction_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_persona, name='agregar_persona'),
    path('lista/', views.lista_personas, name='lista_personas'),
]
