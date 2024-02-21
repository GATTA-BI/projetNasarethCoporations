from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreerUtilisateur 
from django.contrib.auth.decorators import login_required 


# Create your views here.
# @login_required(login_url='acces')
def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form= CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Compte créé avec succès, nom : '+user)

            return redirect('acces')
    context={'form':form}
    return render(request, 'login/inscriptions.html', context)

def accesPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/inscription/inscript')
        else:
            messages.info(request, "Utilisateur et/ou Mot de passe n'existent pas.")
    return render(request, 'login/acces.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')