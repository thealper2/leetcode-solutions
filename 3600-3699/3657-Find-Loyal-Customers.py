import pandas as pd


def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    grouped = customer_transactions.groupby('customer_id')
    results = []

    for customer_id, group in grouped:
        purchases = group[group['transaction_type'] == 'purchase']
        refunds = group[group['transaction_type'] == 'refund']
        num_purchases = len(purchases)
        if num_purchases < 3:
            continue

        num_refunds = len(refunds)
        total_transactions = num_purchases + num_refunds

        group['transaction_date'] = pd.to_datetime(group['transaction_date'])
        min_date = group['transaction_date'].min()
        max_date = group['transaction_date'].max()
        active_days = (max_date - min_date).days
        if active_days < 30:
            continue

        if total_transactions == 0:
            refund_rate = 0
        else:
            refund_rate = num_refunds / total_transactions * 100

        if refund_rate < 20:
            results.append(customer_id)

    result = pd.DataFrame(results, columns=['customer_id'])
    result = result.sort_values('customer_id').reset_index(drop=True)
    return result
