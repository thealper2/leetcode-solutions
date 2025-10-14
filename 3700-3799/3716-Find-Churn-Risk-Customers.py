import pandas as pd

def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    subscription_events['event_date'] = pd.to_datetime(subscription_events['event_date'])
    first_last = subscription_events.groupby('user_id').agg(
        first_date=('event_date', 'min'),
        last_date=('event_date', 'max'),
        last_event=('event_type', lambda x: x.iloc[-1]),
        current_plan=('plan_name', lambda x: x.iloc[-1]),
        current_amount=('monthly_amount', lambda x: x.iloc[-1]),
        max_amount=('monthly_amount', 'max')
    ).reset_index()
    first_last['days_as_subscriber'] = (first_last['last_date'] - first_last['first_date']).dt.days
    downgraders = subscription_events[subscription_events['event_type'] == 'downgrade']['user_id'].unique()
    result = first_last[
        (first_last['last_event'] != 'cancel') &
        (first_last['user_id'].isin(downgraders)) &
        (first_last['current_amount'] < 0.5 * first_last['max_amount']) &
        (first_last['days_as_subscriber'] >= 60)
    ]
    result = result[['user_id', 'current_plan', 'current_amount', 'max_amount', 'days_as_subscriber']] \
             .rename(columns={
                 'current_amount': 'current_monthly_amount',
                 'max_amount': 'max_historical_amount'
             }) \
             .sort_values(by=['days_as_subscriber', 'user_id'], ascending=[False, True]) \
             .reset_index(drop=True)
    return result
