import pandas as pd


def sales_persons(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    merged = pd.merge(company, orders, on="com_id", how="inner")
    return sales_person[
        ~sales_person["sales_id"].isin(merged[merged["name"] == "RED"]["sales_id"])
    ][["name"]]
