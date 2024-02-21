from django.urls import path
from . import views

urlpatterns = [
    path('inscript', views.inscription_home,  name='inscript'),
    path('inscripts', views.inscription_client, name='inscripts'),

]
