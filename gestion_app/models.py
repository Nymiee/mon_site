from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.timezone import now

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
    prenom = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    STATUT_CHOICES = (
        ('Enfant', 'Enfant'),
        ('Orphelin', 'Orphelin'),
    )
    statut = models.CharField(max_length=20, choices=  STATUT_CHOICES,blank=True, null=True) 

    SEXE_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    sexe = models.CharField(max_length=1, choices=  SEXE_CHOICES,blank=True, null=True) 

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
    
    STADE_CHOICES = (
        ('VIH', 'VIH '),
        ('SIDA', 'SIDA'),
    )
    stade = models.CharField(max_length=10, choices=  STADE_CHOICES, blank=True, null=True)

    PAYS_CHOICES = (
        ('Cote d\'Ivoire','Cote d\'Ivoire'),
    )
    pays  = models.CharField(max_length=20, choices=  PAYS_CHOICES,blank=True, null=True) 
    VILLE_CHOICES = (
        ('Abidjan','abidjan'),
        ('Yamoussoukro','Yamoussoukro'),
        ('Bouake','Bouake'),
        ('korogho','korogho'),
    )
    ville = models.CharField(max_length=20, choices=  VILLE_CHOICES,blank=True, null=True) 


    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Lien avec le modèle Utilisateur
    ong = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="enfants")
    inscrit_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="enfants_inscrits", null=True, blank=True)
    date_enregistrement = models.DateTimeField(default=now)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}" if self.prenom else self.nom


class ONG(models.Model):
    nom = models.CharField(max_length=100)
    date_enregistrement = models.DateField()
    date_modification = models.DateTimeField(auto_now=True)

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    date_enregistrement = models.DateField()



class Don(models.Model):
    MOYENS_PAIEMENT = [
        ('mobile_money', 'Mobile Money'),
        ('virement_bancaire', 'Virement Bancaire'),
        ('espece', 'Espèce'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    moyen_paiement = models.CharField(max_length=20, choices=MOYENS_PAIEMENT)
    message = models.TextField(blank=True)
    date_don = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.montant} FCFA"

