import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date'] = pd.to_datetime(trips['trip_date'])
    trips['efficiency'] = trips['distance_km'] / trips['fuel_consumed']
    trips['half'] = trips['trip_date'].dt.month.apply(lambda m: 'first' if m <= 6 else 'second')
    half_avg = trips.groupby(['driver_id', 'half'])['efficiency'].mean().reset_index()
    half_pivot = half_avg.pivot(index='driver_id', columns='half', values='efficiency').reset_index()
    valid_drivers = half_pivot.dropna(subset=['first', 'second'])
    valid_drivers['efficiency_improvement'] = valid_drivers['second'] - valid_drivers['first']
    valid_drivers = valid_drivers[valid_drivers['efficiency_improvement'] >= 0]
    valid_drivers = valid_drivers.round(2)
    result = pd.merge(valid_drivers, drivers, on='driver_id', how='inner')
    result = result.rename(columns={
        'first': 'first_half_avg',
        'second': 'second_half_avg'
    })[['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement']]
    result = result.sort_values(
        by=['efficiency_improvement', 'driver_name'],
        ascending=[False, True]
    ).reset_index(drop=True)
    return result
