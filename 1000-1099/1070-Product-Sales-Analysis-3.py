import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = sales.assign(first_year=sales.groupby("product_id").year.transform(min))
    merged = merged[merged["year"] == merged["first_year"]]
    return merged.merge(product, on="product_id", how="inner")[
        ["product_id", "first_year", "quantity", "price"]
    ]
