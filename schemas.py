from pydantic import BaseModel, Field

class LoanApplicant(BaseModel):
    revolving_utilization: float = Field(..., ge=0, description="Credit utilization ratio")
    age: int = Field(..., ge=18, le=120, description="Age of borrower")
    times_30_59_days_late: int = Field(..., ge=0, description="Times 30-59 days late")
    debt_ratio: float = Field(..., ge=0, description="Monthly debt divided by income")
    monthly_income: float = Field(..., ge=0, description="Monthly income")
    open_credit_lines: int = Field(..., ge=0, description="Number of open credit lines")
    times_90_days_late: int = Field(..., ge=0, description="Times 90+ days late")
    real_estate_loans: int = Field(..., ge=0, description="Number of real estate loans")
    times_60_89_days_late: int = Field(..., ge=0, description="Times 60-89 days late")
    dependents: int = Field(..., ge=0, description="Number of dependents")

class PredictionResponse(BaseModel):
    default_prediction: int
    default_probability: float
    risk_level: str
    