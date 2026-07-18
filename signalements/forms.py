from django import forms 
from .models import Signalements

class SignalementsForm(forms.ModelForm):
    class Meta:
        model =  Signalements
        fields = [
            'titre',
            'description',
            'photo',
            'latitude',
            'longitude',
        ]