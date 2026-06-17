# Endometriosis AI

Production-grade healthcare AI platform for endometriosis risk prediction, explainable machine learning, and clinical decision support.

## Overview

Endometriosis affects approximately 10% of women of reproductive age and often experiences diagnostic delays of several years. This project investigates how machine learning can assist with early risk assessment using clinical symptom data.

The project combines machine learning, explainable AI, and deployment engineering to create an end-to-end healthcare AI system.

## Features

* Exploratory Data Analysis (EDA)
* Logistic Regression Baseline
* Random Forest Benchmark
* XGBoost Classification Model
* SHAP Explainability
* FastAPI REST API
* Swagger Documentation
* Model Serialization with Joblib
* Git-based Version Control

## Dataset

Current MVP uses a structured endometriosis dataset containing:

* Age
* BMI
* Menstrual Irregularity
* Chronic Pain Level
* Hormone Level Abnormality
* Infertility
* Diagnosis Label

Future versions will incorporate longitudinal symptom tracking, imaging data, and biomarker datasets.

## Model Performance

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------- | ------- |
| Logistic Regression | 0.635    | 0.657   |
| Random Forest       | 0.598    | 0.610   |
| XGBoost             | 0.631    | 0.644   |

### Key Finding

Model complexity did not significantly improve performance, suggesting that feature richness is the primary limitation of the current dataset.

## Explainability

SHAP was used to provide clinician-interpretable explanations for model predictions.

Most influential features:

1. Hormone Level Abnormality
2. BMI
3. Chronic Pain Level
4. Infertility
5. Menstrual Irregularity

## API Deployment

The trained model is exposed through a FastAPI REST service.

Example request:

```json
{
  "Age": 32,
  "Menstrual_Irregularity": 1,
  "Chronic_Pain_Level": 8,
  "Hormone_Level_Abnormality": 1,
  "Infertility": 0,
  "BMI": 24
}
```

Example response:

```json
{
  "risk_probability": 0.72,
  "prediction": "High Risk"
}
```

## Project Structure

```text
endometriosis-ai/
├── data/
├── docs/
├── models/
├── notebooks/
├── src/
│   └── api/
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* Pandas
* Scikit-Learn
* XGBoost
* SHAP
* FastAPI
* Joblib
* Jupyter Notebook
* Git/GitHub

## Current Status

Release: v1.0

Completed:

* Data ingestion
* EDA
* Model benchmarking
* Explainable AI
* FastAPI deployment

Planned:

* Dataset V2 integration
* MLflow experiment tracking
* Docker containerization
* Streamlit dashboard
* Multimodal learning
* Clinical data expansion

## Disclaimer

This project is intended for educational and research purposes only and is not a medical device or diagnostic tool.

