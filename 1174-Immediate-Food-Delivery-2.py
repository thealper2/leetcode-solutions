import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # 1 -> immediate, 0 -> scheduled
    delivery = delivery.sort_values(['customer_id', 'order_date'], ascending=[True, True]).drop_duplicates(subset=['customer_id'], keep='first')
    delivery['state'] = np.where((delivery['order_date'] == delivery['customer_pref_delivery_date']), 1, 0)
    return pd.DataFrame({'immediate_percentage': [delivery['state'].mean().round(4) * 100]})
