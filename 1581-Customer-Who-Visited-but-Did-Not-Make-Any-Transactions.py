import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(visits, transactions, on='visit_id', how='left')
    return merged[merged['transaction_id'].isnull()].groupby(by='customer_id', as_index=False).count()[['customer_id', 'visit_id']].sort_values(by='visit_id').rename(columns={'visit_id': 'count_no_trans'})
