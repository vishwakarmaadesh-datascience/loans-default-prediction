from pydantic import BaseModel

class LoanInput(BaseModel):
    revolving_utilization: float
    age: int
    times_30_59_days_late: int
    debt_ratio: float
    monthly_income: float
    open_credit_lines: int
    times_90_days_late: int
    real_estate_loans: int
    times_60_89_days_late: int
    dependents: int