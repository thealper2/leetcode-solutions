import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    return (
        employee.drop_duplicates(subset=["employee_id", "primary_flag"], keep=False)
        .sort_values(by=["employee_id", "primary_flag"], ascending=False)
        .drop_duplicates(subset=["employee_id"], keep="first")[
            ["employee_id", "department_id"]
        ]
    )
