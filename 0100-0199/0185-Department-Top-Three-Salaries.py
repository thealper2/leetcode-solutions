import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    merged = pd.merge(
        employee, department, left_on="departmentId", right_on="id", how="inner"
    )[["id_x", "name_x", "name_y", "salary"]]
    maindf = pd.DataFrame(columns=["id_x", "name_x", "name_y", "salary"])
    for department in merged["name_y"].unique():
        temp_df = merged[merged["name_y"] == department]
        top_3_amounts = sorted(temp_df["salary"].unique(), reverse=True)[:3]
        maindf = pd.concat([maindf, temp_df[temp_df["salary"].isin(top_3_amounts)]])

    return maindf[["name_y", "name_x", "salary"]].rename(
        columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    )
