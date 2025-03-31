import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby("customer_number", as_index=False).count()
    return orders[orders["order_number"] == orders["order_number"].max()][
        ["customer_number"]
    ]
