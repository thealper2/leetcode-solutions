import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.groupby(by=['event_day', 'emp_id'], as_index=False).sum()
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees[['event_day', 'emp_id', 'total_time']].rename(columns={'event_day': 'day'})
