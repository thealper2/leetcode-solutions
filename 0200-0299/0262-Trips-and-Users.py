import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned_users = users[users['banned'] == 'No']['users_id']
    
    valid_trips = trips[
        (trips['client_id'].isin(unbanned_users)) &
        (trips['driver_id'].isin(unbanned_users)) &
        (trips['request_at'].between('2013-10-01', '2013-10-03'))
    ].copy()
    
    if valid_trips.empty:
        return pd.DataFrame(columns=['Day', 'Cancellation Rate'])
    
    valid_trips['is_cancelled'] = valid_trips['status'].isin(['cancelled_by_driver', 'cancelled_by_client'])
    result = valid_trips.groupby('request_at').agg(
        Cancellation_Rate=('is_cancelled', lambda x: round(x.mean(), 2)))
    
    result = result.reset_index()
    result.columns = ['Day', 'Cancellation Rate']
    
    return result