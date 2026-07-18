from django.conf import settings
from django.db import models


class Article(models.Model):
    """Ressource collaborative publiée par un acteur partenaire de la plateforme."""
    TYPE_CHOICES = [
        ('guide', 'Guide'),
        ('livre', 'Livre'),
        ('publication', 'Publication'),
        ('ressource', 'Ressource'),
        ('autre', 'Autre'),
    ]

    ACTEUR_CHOICES = [
        ('autorite', 'Autorité'),
        ('ong', 'ONG'),
        ('ecole', 'École'),
        ('entreprise', 'Entreprise'),
        ('autre', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    sous_titre = models.CharField(max_length=250, blank=True)
    contenu = models.TextField()
    type_ressource = models.CharField(max_length=20, choices=TYPE_CHOICES, default='ressource')
    acteur = models.CharField(max_length=20, choices=ACTEUR_CHOICES, default='autre')
    fichier = models.FileField(upload_to='articles/', blank=True, null=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    categories = models.ManyToManyField('categories.Category', blank=True, related_name='articles')
    date_creation = models.DateTimeField(auto_now_add=True)
    est_publie = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre
