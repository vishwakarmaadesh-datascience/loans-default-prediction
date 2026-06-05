# Loan Default Prediction System

An end-to-end Machine Learning project for predicting loan default risk using FastAPI, Streamlit, and Scikit-learn.

## Features

* Data preprocessing pipeline
* Exploratory Data Analysis (EDA)
* Machine Learning models
* FastAPI backend API
* Streamlit frontend
* Risk prediction with probability scores
* Swagger API documentation

## Tech Stack

* Python
* Pandas
* Scikit-learn
* FastAPI
* Streamlit
* Joblib
* Uvicorn

## Project Structure

```bash
loan-default-pipeline/
│
├── api/
├── frontend/
├── models/
├── notebooks/
├── data/
├── requirements.txt
└── README.md
```

## Run Backend

```bash
uvicorn api.main:app --reload
```

## Run Frontend

```bash
streamlit run frontend/app.py
```

## API Docs

```bash
http://127.0.0.1:8000/docs
```

## Sample Prediction Input

```json
{
  "revolving_utilization": 0.5,
  "age": 45,
  "times_30_59_days_late": 0,
  "debt_ratio": 0.3,
  "monthly_income": 6000,
  "open_credit_lines": 8,
  "times_90_days_late": 0,
  "real_estate_loans": 1,
  "times_60_89_days_late": 0,
  "dependents": 2
}
```
