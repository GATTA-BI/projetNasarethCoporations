from django.urls import path
from . import views

urlpatterns = [
    path('inscriptions', views.inscriptionPage, name='inscriptions'),
    path('acces', views.accesPage, name='acces'),
    # path('Deconnexion', views.logoutUser, name='Deconnexion'),
]