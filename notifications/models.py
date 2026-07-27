from django.db import models 
from django.conf import settings
from signalements.models import Signalements

# Create your models here.

class Notifications(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expediteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications_envoyees')
    signalement =models.ForeignKey(Signalements, on_delete=models.CASCADE, null=True, blank=True)
    titre=models.CharField(max_length=200)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    date_creation=models.DateTimeField(auto_now_add=True)
    url=models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.titre
        
