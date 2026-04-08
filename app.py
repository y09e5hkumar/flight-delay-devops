from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Flight Delay Predictor")

model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

class Flight(BaseModel):
    OP_CARRIER: str
    ORIGIN: str
    DEST: str
    CRS_DEP_TIME: int
    CRS_ARR_TIME: int
    DISTANCE: float

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(flight: Flight):
    df = pd.DataFrame([flight.dict()])
    processed = preprocessor.transform(df)
    pred = model.predict(processed)[0]
    prob = model.predict_proba(processed)[0][1]
    result = {
        "prediction": "Delayed" if pred == 1 else "On Time",
        "delay_probability": round(float(prob), 4)
    }
    logger.info(f"Input: {flight.dict()} | Output: {result}")
    return result