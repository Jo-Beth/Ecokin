from django.conf import settings
from django.db import models

from articles.models import Article


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commentaires')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='reponses')
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    est_valide = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_creation']

    def __str__(self):
        return f'Commentaire de {self.auteur.username} sur {self.article.titre}'
