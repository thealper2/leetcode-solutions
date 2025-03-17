import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(users, transactions, on="account", how="left")[["name", "amount"]]
    merged = (
        merged.groupby("name", as_index=False)
        .agg("sum")
        .rename(columns={"amount": "balance"})
    )
    return merged[merged["balance"] > 10000]
