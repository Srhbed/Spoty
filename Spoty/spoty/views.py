
from datetime import datetime
from django.shortcuts import render
import requests
import csv
import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials 
import os

import requests
import base64
import json
from secrets import *

from pprint import pprint
from . import forms

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{client_id}:{client_secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']



@csrf_exempt

def get_track_info(artist_name, track_name):

    url = "https://api.spotify.com/v1/search"
    params = {
        "q": f"artist:{artist_name} track:{track_name}",
        "type": "track",
        "market":['US','FR'],
        "limit": 10
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    url_img_track= data["tracks"]["items"][0]['album']['images'][0]['url']

    track_id = data["tracks"]["items"][0]["id"]

    info={'album_name':data["tracks"]["items"][0]['album']['name'],
          'release_date':data["tracks"]["items"][0]['album']['release_date'],
          'preview_url':data["tracks"]["items"][0]['preview_url']
          }
   
    pprint(track_id)


    features_url = f"https://api.spotify.com/v1/audio-features/{track_id}"

    data = {'id' : track_id}

    resultat = requests.get(url=features_url, headers=headers, params=data)
    features_items = resultat.json()

    print(features_items)



    feature={
            "duration_ms":features_items["duration_ms"],
            # "release_date":int(track_data['album']['release_date'].split('-')[0]),
            "danceability":features_items["danceability"],
            "energy":features_items["energy"],
            "key":features_items["key"],
            "loudness":features_items["loudness"],
            "mode":features_items["mode"],
            "speechiness":features_items["speechiness"],
            "acousticness":features_items["acousticness"],
            "instrumentalness":features_items["instrumentalness"],
            "liveness":features_items["liveness"],
            "valence":features_items["valence"],
            "tempo":features_items["tempo"],
            "time_signature":features_items["time_signature"],
            # "genre":data["danceability"],
              }


    return feature,url_img_track,info

@csrf_exempt
def search_track(request):
    header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
    
    form = forms.SpotyForm
    if request.method == 'POST':
        form=form(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            artist_name = form.cleaned_data['artist_name']
            track_name = form.cleaned_data['track_name']

            track_info, url , info= get_track_info(artist_name, track_name)
            print(track_info)
            if track_info:
                data = json.dumps(track_info)
                print(data)
                response=requests.post('http://127.0.0.1:8001/predict', headers=header, data=data)
                print(response)
                return render(request, 'result.html', context={'response': response.text, 'form': form, 'url':url,'info':info})
            else:
                form.add_error(None, 'Could not find track')
    else:
        context={'form' : form}
        return render(request, 'home_page.html', context=context)



