from django.db import models
from django.db import models



class  Spotify(models.Model):
    artist_name= models.CharField(
        max_length=100,
    )

    track_name=models.CharField(
             max_length=100,
    )
