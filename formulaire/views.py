from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from formulaire.models import Formulaire
from .forms import FormulaireForm


# Create your views here.


def formulaire_thwo(request, *args, **kwargs):
    formulaire=Formulaire.objects.all()
    context={
        'formulaire':formulaire
    }
    return render(request, 'formulaire/formulaire_thwo.html', context)


def inscription_frond(request, *args, **kwargs):
    if request.method == 'POST':
        form = FormulaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formulaire/form')
    else:
        form = FormulaireForm()
    return render(request, 'formulaire/inscription_frond.html', {'form': form , 'formulaire' : Formulaire.objects.all()})
