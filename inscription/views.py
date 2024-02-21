from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from inscription.models import Inscription
from .forms import InscriptionForm


# Create your views here.


def inscription_home(request, *args, **kwargs):
    inscription=Inscription.objects.all()
    context={
        'inscription':inscription
    }
    return render(request, 'inscription/inscription_home.html', context)


def inscription_client(request, *args, **kwargs):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/inscription/inscript')
    else:
        form = InscriptionForm()
    return render(request, 'inscription/inscription_client.html', {'form': form , 'inscription' : Inscription.objects.all()})
