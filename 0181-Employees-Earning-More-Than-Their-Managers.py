import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        employee,
        employee[["id", "salary"]],
        left_on="managerId",
        right_on="id",
        how="left",
    )
    return df[df["salary_x"] > df["salary_y"]][["name"]].rename(
        columns={"name": "Employee"}
    )
