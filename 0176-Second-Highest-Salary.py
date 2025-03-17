import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee.sort_values(by="salary", ascending=False)[["salary"]]
    if 2 <= salaries["salary"].nunique():
        return pd.DataFrame({"SecondHighestSalary": [salaries["salary"].unique()[1]]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [None]})
