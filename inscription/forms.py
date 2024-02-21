from django.forms import ModelForm
from .models import Inscription

class InscriptionForm(ModelForm):
    class Meta:
        model=Inscription
        # fields=['image_profil', 'nom', 'prenom', 'date_naissance', 'lieu_naissance', 'dernier_diplome', 'fonction', 'telephone', 'email', 'cv']
        fields='__all__'