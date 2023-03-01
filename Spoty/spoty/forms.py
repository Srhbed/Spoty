from django import forms


from . import models



class SpotyForm(forms.ModelForm):
    class Meta:
        model = models.Spotify
        fields = '__all__'
        labels ={
            'artist_name': "Veuillez renseigner le nom de l'artiste",
            'track_name': "Veuillez renseigner le nom du morceau"
        }