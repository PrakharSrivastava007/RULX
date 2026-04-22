from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from predict import predict_all

app = FastAPI(title="RULX API")

# ----------- INPUT MODEL -----------

class SensorInput(BaseModel):
    sequence: List[List[float]]  # shape: (seq_len, features)


# ----------- ROUTES -----------

@app.get("/")
def home():
    return {"message": "RULX API Running"}

@app.post("/predict")
def predict(data: SensorInput):
    result = predict_all(data.sequence)
    return result