from django import forms

from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Écrivez votre commentaire ou suggestion...'}),
        }
