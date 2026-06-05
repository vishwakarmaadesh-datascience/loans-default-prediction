import streamlit as st
import requests

st.title("Loan Default Prediction")

st.write("Enter customer financial details")

revolving_utilization = st.slider(
    "Revolving Utilization",
    0.0, 1.0, 0.5
)

age = st.number_input("Age", 18, 100, 45)

times_30_59_days_late = st.number_input(
    "30-59 Days Late",
    0, 20, 0
)

debt_ratio = st.number_input(
    "Debt Ratio",
    0.0, 10.0, 0.3
)

monthly_income = st.number_input(
    "Monthly Income",
    0.0, 100000.0, 6000.0
)

open_credit_lines = st.number_input(
    "Open Credit Lines",
    0, 50, 8
)

times_90_days_late = st.number_input(
    "90 Days Late",
    0, 20, 0
)

real_estate_loans = st.number_input(
    "Real Estate Loans",
    0, 20, 1
)

times_60_89_days_late = st.number_input(
    "60-89 Days Late",
    0, 20, 0
)

dependents = st.number_input(
    "Dependents",
    0, 10, 2
)

if st.button("Predict Default Risk"):

    payload = {
        "revolving_utilization": revolving_utilization,
        "age": age,
        "times_30_59_days_late": times_30_59_days_late,
        "debt_ratio": debt_ratio,
        "monthly_income": monthly_income,
        "open_credit_lines": open_credit_lines,
        "times_90_days_late": times_90_days_late,
        "real_estate_loans": real_estate_loans,
        "times_60_89_days_late": times_60_89_days_late,
        "dependents": dependents
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    result = response.json()

    st.subheader("Prediction Result")

    st.write(
        f"Default Prediction: {result['default_prediction']}"
    )

    st.write(
        f"Default Probability: {result['default_probability']}"
    )

    st.write(
        f"Risk Level: {result['risk_level']}"
    )