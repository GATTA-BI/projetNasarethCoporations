from django.forms import ModelForm
from .models import Formulaire

class FormulaireForm(ModelForm):
    class Meta:
        model=Formulaire
        # fields=['image_profil', 'nom', 'prenom', 'date_naissance', 'lieu_naissance', 'dernier_diplome', 'fonction', 'telephone', 'email', 'cv']
        fields='__all__'