import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product, on="product_id", how="inner")[
        ["product_name", "year", "price"]
    ]
