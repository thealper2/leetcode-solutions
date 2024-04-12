import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = orders[(orders['order_date'].dt.month == 2) & (orders['order_date'].dt.year == 2020)].groupby(by='product_id', as_index=False)[['unit']].sum()
    merged = merged[merged['unit'] >= 100]
    return pd.merge(products, merged, on='product_id', how='inner')[['product_name', 'unit']]
