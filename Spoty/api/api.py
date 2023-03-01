import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# with open('xgb.pkl','rb') as file:
#     xgb = pickle.load(file)

import joblib
pickle_in = open('xgb.pkl', 'rb') 
xgb = joblib.load(pickle_in)


app = FastAPI()

class request(BaseModel):
    # track_number : float
    # genre :str
    duration_ms:float
    # release_date: float
    danceability : float
    energy : float
    key : float
    loudness : float
    mode : float
    speechiness :float
    acousticness : float
    instrumentalness : float
    liveness : float
    valence : float
    tempo: float
    time_signature:float


    
@app.post("/predict")
    
def predict(data:request):
    new_data=pd.DataFrame(dict(data),index = [0])
    print(new_data)
    class_idx=xgb.predict(new_data)
    return float(class_idx)
