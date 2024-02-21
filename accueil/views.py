from django.shortcuts import render

# Create your views here.
def accueil_home(request):
    return render(request, 'accueil/accueil_menu.html')
