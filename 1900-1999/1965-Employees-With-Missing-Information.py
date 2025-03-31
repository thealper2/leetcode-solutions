import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, salaries, on="employee_id", how="outer")
    mask = (merged["name"].isnull()) | (merged["salary"].isnull())
    return merged[mask][["employee_id"]]
