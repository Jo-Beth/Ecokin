from django.contrib import admin

from .models import Commentaire


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('article', 'auteur', 'date_creation', 'est_valide')
    list_filter = ('est_valide',)
    search_fields = ('contenu', 'auteur__username')
