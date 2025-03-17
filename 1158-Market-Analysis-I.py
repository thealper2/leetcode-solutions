import pandas as pd


def market_analysis(
    users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame
) -> pd.DataFrame:
    merged1 = pd.merge(
        users, orders, left_on="user_id", right_on="buyer_id", how="left"
    )
    merged2 = pd.merge(items, merged1, on="item_id", how="left")
    all_users = users["user_id"].unique()
    filtered = merged2[merged2["order_date"].dt.year == 2019]
    filtered = (
        filtered.groupby("user_id")
        .size()
        .reindex(all_users, fill_value=0)
        .reset_index(drop=True)
    )
    result = pd.concat([users[["user_id", "join_date"]], filtered], axis=1)
    result.columns = ["buyer_id", "join_date", "orders_in_2019"]
    return result
