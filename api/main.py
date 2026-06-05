from fastapi import FastAPI
from .schemas import LoanInput
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/best_pipeline.pkl")


@app.get("/")
def home():
    return {"message": "API running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: LoanInput):

    input_data = pd.DataFrame([{
        "RevolvingUtilizationOfUnsecuredLines": data.revolving_utilization,
        "age": data.age,
        "NumberOfTime30-59DaysPastDueNotWorse": data.times_30_59_days_late,
        "DebtRatio": data.debt_ratio,
        "MonthlyIncome": data.monthly_income,
        "NumberOfOpenCreditLinesAndLoans": data.open_credit_lines,
        "NumberOfTimes90DaysLate": data.times_90_days_late,
        "NumberRealEstateLoansOrLines": data.real_estate_loans,
        "NumberOfTime60-89DaysPastDueNotWorse": data.times_60_89_days_late,
        "NumberOfDependents": data.dependents
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    if probability < 0.3:
        risk_level = "Low"
    elif probability < 0.7:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "default_prediction": int(prediction),
        "default_probability": float(probability),
        "risk_level": risk_level
    }