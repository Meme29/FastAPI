"""
* A POST route that takes this dictionary (in `json` format) and returns the computation of `salary + bonus - taxes`.
* Make sure to return an error if the user enters a string instead  of a number.
* Make sure the user sends the 3 fields.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SalaryInput(BaseModel):
    salary: float
    bonus: float
    taxes: float

@router.post("/salary", tags=["Salary"])
def compute_salary(salary_input: SalaryInput):
    try:
        result = salary_input.salary + salary_input.bonus - salary_input.taxes
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="expected numbers, got strings.")
    except Exception as e:
        missing_fields = []
        if not salary_input.salary:
            missing_fields.append("salary")
        if not salary_input.bonus:
            missing_fields.append("bonus")
        if not salary_input.taxes:
            missing_fields.append("taxes")
        if missing_fields: # Raise missing fields error if any field is missing
            raise HTTPException(status_code=400, detail=f"3 fields expected (salary, bonus, taxes). You forgot: {', '.join(missing_fields)}.")
        # For any other exceptions, raise a generic error
        raise HTTPException(status_code=400, detail=str(e))