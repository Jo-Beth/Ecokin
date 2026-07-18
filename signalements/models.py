from django.db import models
from django.conf import settings

# Create your models here.
class categories(models.Model):
    """Catégorie associée à un signalement, utilisée pour classifier les problèmes."""
    nom = models.CharField(max_length =100, blank = True, help_text= "Veuillez saisir la catégories")
    
    def __str__ (self):
        return self.nom

class Signalements(models.Model):
    """Signalement environnemental soumis par un citoyen et traité par les acteurs concernés."""
    
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
        ('rejete', 'Rejeté'),
    ]
    
    titre = models.CharField(max_length=200, help_text="Entrez le titre du signalement")
    description = models.TextField()
    photo = models.ImageField(upload_to = 'signalements/', blank=True, null=True)
    latitude = models.DecimalField(max_digits= 9, decimal_places= 6)
    longitude = models.DecimalField(max_digits= 9, decimal_places= 6)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_creation = models.DateField(auto_now_add= True)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'signalements')
    
    def __str__(self):
        return self.titre
    
    def peut_etre_modifier(self):
        return self.statut == "en_attente"
    
    def peut_etre_supprimer(self):
        return self.statut == "en_attente"
    
    def changer_statut(self, nouvel_statut):
        self.statut = nouvel_statut
        self.save()
        