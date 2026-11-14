# Loan Default Prediction System

An end-to-end Machine Learning application that predicts customer loan default risk using financial and credit-related information. The project integrates machine learning pipelines, experiment tracking, REST API development and an interactive Streamlit frontend to provide probability-based financial risk assessment.

## Project Overview

Loan default prediction is an important problem in financial risk management. Banks and financial institutions need to evaluate borrowers' credit behavior and financial characteristics to estimate the possibility of repayment failure.

This project develops a machine learning-based loan default prediction system that analyzes customer financial information and estimates the likelihood of default within the next two years.

The application combines a trained classification pipeline with a FastAPI backend and Streamlit frontend to provide an interactive prediction workflow.

## Key Features

- **Loan Default Prediction:** Predicts whether a customer is likely to default on a loan.
- **Exploratory Data Analysis:** Identifies patterns, distributions, correlations and financial risk indicators.
- **Data Preprocessing:** Handles missing values, duplicates, outliers and numerical feature transformations.
- **Feature Engineering:** Prepares financial and credit-related variables for machine learning.
- **Machine Learning Model Comparison:** Implements and compares multiple classification algorithms.
- **Scikit-learn Pipelines:** Uses Pipeline and ColumnTransformer for consistent preprocessing and model inference.
- **MLflow Experiment Tracking:** Tracks machine learning experiments and model performance.
- **Probability-Based Risk Assessment:** Generates default probability scores and categorizes predictions into Low, Medium and High risk levels.
- **REST API Integration:** Uses FastAPI to expose prediction functionality through HTTP endpoints.
- **Interactive Frontend:** Uses Streamlit to collect customer information and display prediction results.

## Dataset Information

The project uses the `cs-training.csv` dataset, containing approximately 150,000 customer records with financial and credit-related attributes.

**Target Variable**

| Feature | Description |
|---|---|
| `SeriousDlqin2yrs` | Indicates whether a customer experienced serious delinquency within two years |

**Input Features**

| Feature | Description |
|---|---|
| RevolvingUtilizationOfUnsecuredLines | Credit utilization ratio |
| age | Customer age |
| NumberOfTime30-59DaysPastDueNotWorse | Number of payments 30–59 days past due |
| DebtRatio | Customer debt ratio |
| MonthlyIncome | Customer monthly income |
| NumberOfOpenCreditLinesAndLoans | Number of open credit lines and loans |
| NumberOfTimes90DaysLate | Number of payments 90 or more days late |
| NumberRealEstateLoansOrLines | Number of real estate loans or credit lines |
| NumberOfTime60-89DaysPastDueNotWorse | Number of payments 60–89 days past due |
| NumberOfDependents | Number of customer dependents |

## Machine Learning Workflow

### 1. Data Collection
- Importing the structured credit-risk dataset.
- Understanding the dataset structure and target variable.
- Examining numerical and financial attributes.

### 2. Exploratory Data Analysis (EDA)
- Univariate and bivariate analysis.
- Distribution analysis of financial variables.
- Correlation analysis.
- Default and non-default class distribution.
- Identification of outliers and unusual observations.

### 3. Data Preprocessing
- Handling missing values.
- Checking duplicate records.
- Outlier investigation and treatment.
- Numerical feature preparation.
- Feature scaling.

### 4. Model Development

The following classification algorithms were implemented and compared:

| Algorithm | Purpose |
|---|---|
| Logistic Regression | Baseline binary classification |
| Random Forest Classifier | Ensemble-based classification |
| Gradient Boosting Classifier | Boosting-based classification |

### 5. Pipeline Development

Scikit-learn preprocessing and modeling components were integrated using:

- `Pipeline`
- `ColumnTransformer`
- `StandardScaler`

This helps maintain consistent data transformations between model training and prediction.

### 6. Model Evaluation

The models are evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The evaluation process helps compare classification performance and understand the trade-offs between identifying defaulting and non-defaulting customers.

### 7. Model Experiment Tracking

MLflow is used for tracking model experiments, comparing model performance and maintaining experiment records.

### 8. Model Deployment

The selected trained model pipeline is serialized using Joblib and integrated into a FastAPI backend.

## Probability-Based Risk Classification

The application uses the predicted default probability to categorize customers into risk levels.

| Default Probability | Risk Category |
|---|---|
| Below 0.30 | Low Risk |
| 0.30 to below 0.70 | Medium Risk |
| 0.70 and above | High Risk |

These are application-defined thresholds and are not independently validated lending or regulatory risk cutoffs.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| ML Experiment Tracking | MLflow |
| Model Serialization | Joblib |
| Backend Development | FastAPI |
| API Server | Uvicorn |
| Frontend Development | Streamlit |
| API Communication | Requests |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

## Project Architecture

The project follows a modular architecture separating the machine learning workflow, backend API and frontend application.

```text
Loan-Default-Prediction-System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routes.py
│
├── frontend/
│   ├── app.py
│   └── assets/
│
├── models/
│   ├── best_pipeline.pkl
│   └── model_metadata.json
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── prediction.py
│   ├── model_loader.py
│   └── utils.py
│
├── notebooks/
│   └── loansdefault.ipynb
│
├── data/
│   ├── raw/
│   │   └── cs-training.csv
│   └── processed/
│
├── tests/
│   ├── test_api.py
│   └── test_prediction.py
│
└── mlruns/
```

*Note: This represents the intended organized project structure. Update the tree to match the final uploaded repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vishwakarmaadesh-datascience/loans-default-prediction.git
```

### 2. Navigate to the Project

```bash
cd loans-default-prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI Backend

After placing the API entry point in `api/main.py`:

```bash
uvicorn api.main:app --reload
```

### 7. Access API Documentation

FastAPI provides interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 8. Run the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

**Note:** The trained model artifact must be present at the path expected by the API before starting the backend. The frontend must also be configured to communicate with the running API.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome and status message |
| GET | `/health` | Backend health check |
| POST | `/predict` | Generate loan default prediction |

### Sample API Request

Endpoint:

```text
POST /predict
```

Request body:

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

### Sample API Response

```json
{
  "default_prediction": 0,
  "default_probability": 0.18,
  "risk_level": "Low"
}
```

*Illustrative response only; actual predictions depend on the trained model and supplied input.*

## Future Improvements

- Deploy the application using Docker.
- Host the frontend and backend on cloud infrastructure.
- Implement model monitoring and drift detection.
- Introduce SHAP or LIME for model explainability.
- Develop automated model retraining pipelines.
- Implement authentication and secure API access.
- Improve probability calibration and threshold selection.
- Integrate CI/CD workflows for automated testing and deployment.

## Important Disclaimer

This project is developed for educational, academic and portfolio purposes.

The predictions represent estimates generated by machine learning models trained on historical data. They should not be treated as definitive credit decisions, financial advice or a substitute for professional credit-risk assessment.

## Author

**Adesh Vishwakarma**

MSc Data Science Student | BSc Data Science Graduate | Aspiring Machine Learning Engineer

- **GitHub:** [vishwakarmaadesh-datascience](https://github.com/vishwakarmaadesh-datascience)
- **LinkedIn:** [Adesh Vishwakarma](https://www.linkedin.com/in/adesh-vishwakarma-53108b324/)

---

*Developed as an end-to-end Machine Learning and Financial Risk Analytics project.*
