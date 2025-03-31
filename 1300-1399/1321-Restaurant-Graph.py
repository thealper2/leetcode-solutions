import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = (
        customer.sort_values(by="visited_on")
        .groupby(by="visited_on", as_index=False)[["amount"]]
        .sum()
    )
    customer["amount"] = customer["amount"].rolling(window=7).sum()
    customer = customer.dropna(subset=["amount"])
    customer["average_amount"] = round(customer["amount"] / 7, 2)
    return customer
