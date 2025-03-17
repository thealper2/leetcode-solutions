import pandas as pd


def confirmation_rate(
    signups: pd.DataFrame, confirmations: pd.DataFrame
) -> pd.DataFrame:
    confirmations["confirmation_rate"] = confirmations["action"].apply(
        lambda x: 1 if x == "confirmed" else 0
    )
    average_confirmation_rate = (
        confirmations[["user_id", "confirmation_rate"]]
        .groupby("user_id")[["confirmation_rate"]]
        .mean()
        .round(2)
        .reset_index()
    )
    return pd.merge(signups["user_id"], average_confirmation_rate, how="left").fillna(0)
