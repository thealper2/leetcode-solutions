import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    dated = products[products['change_date'] <= pd.to_datetime('2019-08-16')].sort_values(by='change_date', ascending=True).drop_duplicates(subset=['product_id'],keep='last')[['product_id', 'new_price']]
    not_in = products[~products['product_id'].isin(dated['product_id'].unique())][['product_id', 'new_price']]
    not_in['new_price'] = 10
    return pd.concat([dated, not_in], axis=0).rename(columns={'new_price': 'price'}).drop_duplicates(keep='last').sort_values(by='product_id', ascending=True)
