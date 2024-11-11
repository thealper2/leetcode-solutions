import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    result = transactions.groupby('transaction_date').apply(
        lambda x: pd.Series({
            'odd_sum': x.loc[x['amount'] % 2 != 0, 'amount'].sum(),
            'even_sum': x.loc[x['amount'] % 2 == 0, 'amount'].sum()
        })
    ).reset_index()
    return result