from django.db import models

# Create your models here.
class Formulaire(models.Model):

    CYCLES=(('Premier Cycle','Premier Cycle'),
             ('Second Cycle', 'Second Cycle'),
             ('Cycle Superieur', 'Cycle Superieur'))

    Denomination_etablissement= models.CharField(max_length=3000, null=True)
    Code=models.CharField(max_length=3000, null=True)
    Nom_prenom_directeur=models.CharField(max_length=3000, null=True)
    Nom_prenom_fondateur=models.CharField(max_length=3000, null=True)
    Nombre_enseignants=models.IntegerField(max_length=3000, null=True)
    Cycle=models.CharField(max_length=3000, null=True, choices=CYCLES)
    Localisation=models.CharField(max_length=3000, null=True)
    Drena=models.CharField(max_length=3000, null=True)
    Contacts=models.CharField(max_length=3000, null=True)
    date=models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        verbose_name=("Formulaire")
        verbose_name_plural=("Formulaires")

    def __str__(self):
        return self.Denomination_etablissement
 