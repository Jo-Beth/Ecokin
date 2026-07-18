from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'sous_titre', 'contenu', 'type_ressource', 'acteur', 'categories', 'fichier']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'sous_titre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'type_ressource': forms.Select(attrs={'class': 'form-control'}),
            'acteur': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fichier': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
