import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["approved_count"] = np.where(
        (transactions["state"] == "approved"), 1, 0
    )
    transactions["declined_count"] = np.where(
        (transactions["state"] == "declined"), 1, 0
    )
    transactions["month"] = transactions["trans_date"].apply(
        lambda x: x.strftime("%Y-%m")
    )
    transactions = transactions[
        ["month", "country", "approved_count", "declined_count", "amount"]
    ]
    transactions["trans_count"] = (
        transactions["approved_count"] + transactions["declined_count"]
    )
    transactions["approved_total_amount"] = (
        transactions["approved_count"] * transactions["amount"]
    )
    return (
        transactions.groupby(by=["month", "country"], as_index=False, dropna=False)
        .agg(
            {
                "trans_count": "sum",
                "approved_count": "sum",
                "amount": "sum",
                "approved_total_amount": "sum",
            }
        )
        .rename(columns={"amount": "trans_total_amount"})
    )
