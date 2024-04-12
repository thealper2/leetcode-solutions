import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = customer.drop_duplicates().groupby(by='customer_id', as_index=False).size()
    return merged[merged['size'] == product['product_key'].nunique()][['customer_id']]
