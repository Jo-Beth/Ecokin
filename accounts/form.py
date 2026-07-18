from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "telephone",
            "adresse",
            "photo",
            "password1",
            "password2",
        ]
  