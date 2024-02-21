from django.db import models

# Create your models here.
class Inscription(models.Model):

    MATIERE=(('Professeur','Professeur'),
             ('Professeure', 'Professeure'),
             ('Educatrice', 'Educatrice'),
             ('Educateur', 'Educateur'))

    photo_profil = models.ImageField(upload_to='photos', blank=True)
    nom=models.CharField(max_length=3000, null=True)
    prenom=models.CharField(max_length=3000, null=True)
    date_naissance=models.DateField(null=True)
    lieu_naissance=models.CharField(max_length=3000, null=True)
    dernier_diplome=models.CharField(max_length=3000, null=True)
    fonction=models.CharField(max_length=3000, null=True, choices=MATIERE)
    telephone=models.CharField (max_length=3000, null=True)
    email=models.EmailField(max_length=3000, null=True)
    cv=models.FileField(upload_to='documents',max_length=3000, null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name=("Inscription")
        verbose_name_plural=("Inscriptions")

    def __str__(self):
        return self.nom
 