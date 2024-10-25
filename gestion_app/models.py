from django.db import models
from django.contrib.auth.models import AbstractUser



class Utilisateur(AbstractUser):
    USER_TYPE_CHOICES = (
        ('doctor', 'Médecin'),
        ('ong', 'ONG'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username

class Enfant(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)  # Ajout du champ prénom
    age = models.IntegerField()
    SEXE_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    sexe = models.CharField(max_length=10, choices=  SEXE_CHOICES,blank=True, null=True) 
    GROUPE_SANGUIN_CHOICES = (
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),   
    )
    groupe_sanguin = models.CharField(max_length=10, choices=  GROUPE_SANGUIN_CHOICES,blank=True, null=True)  # Ajout du champ groupe sanguin
    
    STATUT_CHOICES = (
        ('Diagnostic positif', 'Diagnostic positif'),
        ('Exposition au VIH', 'Exposition au VIH'),
    )
    statut = models.CharField(max_length=20, choices=  STATUT_CHOICES, blank=True, null=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Lien avec le modèle Utilisateur

    def __str__(self):
        return f"{self.prenom} {self.nom}" if self.prenom else self.nom


