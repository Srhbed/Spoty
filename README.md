# Les Gens N'ont Plus de Goût 

Les gens n'ont plus de goût est une application web qui permet de prédire la popularité d'un morceau de musique s'il avait été sorti en 2022 en se basant sur ses caractéristiques musicales. Cette application utilise un modèle de prédiction de popularité qui a été entraîné sur des données de morceaux de musique récents. 

* Fonctionnalités :
    - Authentification : les utilisateurs peuvent créer un compte et se connecter à l'application. 
    - Page de profil : les utilisateurs peuvent modifier leur nom d'utilisateur et leur mot de passe. 
    - Recherche de musique : les utilisateurs peuvent rechercher des morceaux de musique en utilisant le formulaire de recherche. 
    - Prédiction de popularité : les utilisateurs peuvent obtenir une prédiction de popularité pour un morceau de musique en utilisant le formulaire de prédiction. 

  

* Installation

   -  Cloner le dépôt git : git clone https://github.com/Srhbed/Spoty.git
   - Construire les containers Docker : docker-compose up --build
   - Accéder à l'application à l'adresse http://20.8.138.55/

* Dépendances

    - Python 
    - Django 
    - Scikit-learn 
    - Spotipy 
    - Docker 

* Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez apporter des modifications à l'application, veuillez suivre les étapes suivantes :

    Créer une branche à partir de la branche main
    Effectuer les modifications nécessaires
    Créer une pull request vers la branche main

* API 

L'application expose une API qui permet d'obtenir une prédiction de popularité pour un morceau de musique en utilisant une requête POST .

Les données doivent être envoyées au format JSON dans le corps de la requête. Les données doivent inclure les caractéristiques musicales du morceau de musique que vous souhaitez prédire. 

Exemple de données JSON : 

        json 

            {
                "acousticness": 0.234,
                "danceability": 0.756,
                "duration_ms": 205920,
                "energy": 0.543,
                "instrumentalness": 0,
                "key": 2,
                "liveness": 0.134,
                "loudness": -7.32,
                "mode": 1,
                "speechiness": 0.0356,
                "tempo": 120.03,
                "time_signature": 4,
                "valence": 0.624
            }


* Base de données 
L'application utilise une base de données SQLite3
