from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil_home),
]