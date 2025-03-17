import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, on="empId", how="left")
    return merged[(merged["bonus"].isnull()) | (merged["bonus"] < 1000)][
        ["name", "bonus"]
    ]
