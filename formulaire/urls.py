from django.urls import path
from . import views

urlpatterns = [
    path('form', views.formulaire_thwo, name='form'),
    path('forme', views.inscription_frond, name='forme'),

]