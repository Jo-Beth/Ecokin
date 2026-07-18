from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):
    """Utilisateur personnalisé de la plateforme Écokin avec rôles et droits spécifiques."""
    
    ROLE_CHOICES = [
        ('citoyens', 'Citoyens'),
        ('autorités', 'Autorités'),
        ('ong', 'Ong'),
        ('admin', 'Administrateur'),
        
    ]
    
    telephone = models.CharField(max_length= 50, blank=True, help_text="Entrez votre numero ici")
    adresse = models.CharField(max_length= 255, blank=True, help_text="Entrez votre adresse ici")
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citoyens')
    
    def __str__(self):
        return self.username
    
    def est_autorite(self):
        return self.role == "autorités"
    
    def peut_etre_modifier(self,signalements):
        return (
            self == signalements.utilisateur or self.est_autorite()
        )
     
    def peut_etre_supprimer(self, signalements):
         return(
             self == signalements.utilisateur or self.est_autorite()
         )
    @property
         
    def peut_changer_satut(self):
        return self.role == "autorités" 
    
