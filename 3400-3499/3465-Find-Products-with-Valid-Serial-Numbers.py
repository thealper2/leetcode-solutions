import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    pattern = r'SN\d{4}-\d{4}(?:\W|$)'
    valid_products = products[products['description'].str.contains(pattern, regex=True)].copy()
    valid_products = valid_products.sort_values('product_id', ascending=True)
    return valid_products