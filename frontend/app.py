import os

import requests
import streamlit as st

st.set_page_config(page_title="Loan Default Prediction")


def get_api_url():
    try:
        return st.secrets["API_URL"].rstrip("/")
    except Exception:
        return os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")


st.title("Loan Default Prediction")
st.write("Enter customer financial details")

revolving_utilization = st.slider("Revolving Utilization", 0.0, 1.0, 0.5)
age = st.number_input("Age", 18, 100, 45)
times_30_59_days_late = st.number_input("30-59 Days Late", 0, 20, 0)
debt_ratio = st.number_input("Debt Ratio", 0.0, 10.0, 0.3)
monthly_income = st.number_input("Monthly Income", 0.0, 100000.0, 6000.0)
open_credit_lines = st.number_input("Open Credit Lines", 0, 50, 8)
times_90_days_late = st.number_input("90 Days Late", 0, 20, 0)
real_estate_loans = st.number_input("Real Estate Loans", 0, 20, 1)
times_60_89_days_late = st.number_input("60-89 Days Late", 0, 20, 0)
dependents = st.number_input("Dependents", 0, 10, 2)

if st.button("Predict Default Risk", type="primary"):
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
        "dependents": dependents,
    }
    try:
        with st.spinner("Contacting the API (the first call can take up to a minute)..."):
            response = requests.post(f"{get_api_url()}/predict", json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()
    except requests.RequestException as e:
        st.error(f"Could not reach the prediction API: {e}")
        st.stop()

    st.subheader("Prediction Result")
    col1, col2, col3 = st.columns(3)
    col1.metric("Default prediction", "Default" if result["default_prediction"] else "No default")
    col2.metric("Default probability", f"{result['default_probability']:.1%}")
    col3.metric("Risk level", result["risk_level"])
