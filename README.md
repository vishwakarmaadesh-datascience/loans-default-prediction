# Loan Default Prediction System

An end-to-end Machine Learning project for predicting loan default risk using Scikit-learn, FastAPI, and Streamlit.

The system analyzes customer financial information and predicts whether a customer is likely to default on a loan, along with probability-based risk assessment.

---

# Project Overview

This project simulates a real-world financial risk assessment system used in banks and fintech companies.

The project includes:
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Machine Learning model training
- Scikit-learn Pipelines
- FastAPI backend APIs
- Streamlit frontend application
- Real-time prediction system

---

# Dataset Information

The dataset contains customer financial and credit-related information used for predicting loan default behavior.

## Dataset Features

| Feature | Description |
|---|---|
| RevolvingUtilizationOfUnsecuredLines | Credit utilization ratio |
| age | Customer age |
| NumberOfTime30-59DaysPastDueNotWorse | Number of late payments (30–59 days) |
| DebtRatio | Monthly debt ratio |
| MonthlyIncome | Monthly income of customer |
| NumberOfOpenCreditLinesAndLoans | Total active credit lines |
| NumberOfTimes90DaysLate | Number of 90+ days late payments |
| NumberRealEstateLoansOrLines | Real estate loans count |
| NumberOfTime60-89DaysPastDueNotWorse | Number of 60–89 days late payments |
| NumberOfDependents | Number of dependents |

## Target Variable

| Target | Meaning |
|---|---|
| SeriousDlqin2yrs | Whether customer defaulted within 2 years |

## Dataset Size

- ~150,000 records
- Binary Classification Dataset
- Financial Risk Prediction Problem

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Uvicorn
- Git & GitHub

---

# Machine Learning Workflow

## 1. Data Cleaning
- Removed unnecessary columns
- Handled missing values
- Checked duplicates and outliers

## 2. Exploratory Data Analysis
- Distribution analysis
- Correlation analysis
- Default rate visualization
- Risk trend analysis

## 3. Feature Engineering
- Numerical preprocessing
- Standard scaling
- Column transformations

## 4. Model Training

Implemented and compared:
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

## 5. Pipeline Creation

Used:
- Pipeline
- ColumnTransformer
- StandardScaler

for scalable preprocessing and inference.

---

# Backend API (FastAPI)

The backend API provides:
- Real-time loan default prediction
- Probability scoring
- Risk level classification

## Run Backend

```bash
uvicorn api.main:app --reload
```

## Swagger API Docs

```bash
http://127.0.0.1:8000/docs
```

---

# Frontend Application (Streamlit)

Interactive frontend built using Streamlit for:
- User input collection
- Risk prediction
- Probability visualization

## Run Frontend

```bash
streamlit run frontend/app.py
```

---

# Sample API Input

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

---

# Project Structure

```bash
loan-default-pipeline/
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── __init__.py
│
├── frontend/
│   └── app.py
│
├── models/
│
├── notebooks/
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---
#Images of Accuracy of Logistic Regression,Gradient Boosting and Random Forest
<img width="1083" height="655" alt="loansdefault-modelaccuracy" src="https://github.com/user-attachments/assets/374dd010-4b52-4c71-bc03-0d74ee469a5f" />

# Key Features

- End-to-end ML pipeline
- Real-time prediction system
- REST API integration
- Interactive frontend UI
- Deployment-ready architecture
- Risk probability scoring

---

# Future Improvements

- Docker deployment
- Cloud deployment (AWS/GCP/Azure)
- Model monitoring
- CI/CD integration
- Authentication system
- Advanced explainability using SHAP/LIME

---

# Author

Adesh Vishwakarma

GitHub:
https://github.com/vishwakarmaadesh-datascience
vishwakarmaadesh90@gmail.com
