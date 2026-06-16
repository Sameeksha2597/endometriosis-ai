from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "endometriosis_model.pkl"

print("Loading model from:")
print(MODEL_PATH)

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Endometriosis Risk Prediction API"
)

# Input schema
class PatientData(BaseModel):
    Age: int
    Menstrual_Irregularity: int
    Chronic_Pain_Level: float
    Hormone_Level_Abnormality: int
    Infertility: int
    BMI: float


@app.get("/")
def home():
    return {
        "message": "Endometriosis Prediction API Running"
    }


@app.post("/predict")
def predict(data: PatientData):

    input_df = pd.DataFrame([{
        "Age": data.Age,
        "Menstrual_Irregularity": data.Menstrual_Irregularity,
        "Chronic_Pain_Level": data.Chronic_Pain_Level,
        "Hormone_Level_Abnormality": data.Hormone_Level_Abnormality,
        "Infertility": data.Infertility,
        "BMI": data.BMI
    }])

    probability = model.predict_proba(input_df)[0][1]

    prediction = (
        "High Risk"
        if probability >= 0.5
        else "Low Risk"
    )

    return {
        "risk_probability": round(float(probability), 4),
        "prediction": prediction
    }