import joblib
import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Test 1 - Model loads correctly
def test_model_loads():
    pipeline = joblib.load("models/best_pipeline.pkl")
    assert pipeline is not None

# Test 2 - Model predicts correct output shape
def test_model_output_shape():
    pipeline = joblib.load("models/best_pipeline.pkl")
    sample = pd.DataFrame([{
        "RevolvingUtilizationOfUnsecuredLines": 0.5,
        "age": 45,
        "NumberOfTime30-59DaysPastDueNotWorse": 0,
        "DebtRatio": 0.3,
        "MonthlyIncome": 6000,
        "NumberOfOpenCreditLinesAndLoans": 8,
        "NumberOfTimes90DaysLate": 0,
        "NumberRealEstateLoansOrLines": 1,
        "NumberOfTime60-89DaysPastDueNotWorse": 0,
        "NumberOfDependents": 2
    }])
    prediction = pipeline.predict(sample)
    assert len(prediction) == 1
    assert prediction[0] in [0, 1]

# Test 3 - Probability is between 0 and 1
def test_model_probability_range():
    pipeline = joblib.load("models/best_pipeline.pkl")
    sample = pd.DataFrame([{
        "RevolvingUtilizationOfUnsecuredLines": 0.5,
        "age": 45,
        "NumberOfTime30-59DaysPastDueNotWorse": 0,
        "DebtRatio": 0.3,
        "MonthlyIncome": 6000,
        "NumberOfOpenCreditLinesAndLoans": 8,
        "NumberOfTimes90DaysLate": 0,
        "NumberRealEstateLoansOrLines": 1,
        "NumberOfTime60-89DaysPastDueNotWorse": 0,
        "NumberOfDependents": 2
    }])
    proba = pipeline.predict_proba(sample)[0]
    assert 0 <= proba[0] <= 1
    assert 0 <= proba[1] <= 1
    assert round(proba[0] + proba[1], 5) == 1.0

# Test 4 - Batch prediction works
def test_model_batch_prediction():
    pipeline = joblib.load("models/best_pipeline.pkl")
    batch = pd.DataFrame([
        {
            "RevolvingUtilizationOfUnsecuredLines": 0.5,
            "age": 45,
            "NumberOfTime30-59DaysPastDueNotWorse": 0,
            "DebtRatio": 0.3,
            "MonthlyIncome": 6000,
            "NumberOfOpenCreditLinesAndLoans": 8,
            "NumberOfTimes90DaysLate": 0,
            "NumberRealEstateLoansOrLines": 1,
            "NumberOfTime60-89DaysPastDueNotWorse": 0,
            "NumberOfDependents": 2
        },
        {
            "RevolvingUtilizationOfUnsecuredLines": 0.99,
            "age": 25,
            "NumberOfTime30-59DaysPastDueNotWorse": 5,
            "DebtRatio": 0.9,
            "MonthlyIncome": 1000,
            "NumberOfOpenCreditLinesAndLoans": 15,
            "NumberOfTimes90DaysLate": 10,
            "NumberRealEstateLoansOrLines": 0,
            "NumberOfTime60-89DaysPastDueNotWorse": 5,
            "NumberOfDependents": 4
        }
    ])
    predictions = pipeline.predict(batch)
    assert len(predictions) == 2