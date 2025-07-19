import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    meetings['meeting_date'] = pd.to_datetime(meetings['meeting_date'])
    meetings['year'] = meetings['meeting_date'].dt.isocalendar().year
    meetings['week'] = meetings['meeting_date'].dt.isocalendar().week
    weekly_meeting_hours = meetings.groupby(['employee_id', 'year', 'week'])['duration_hours'].sum().reset_index()
    meeting_heavy_weeks = weekly_meeting_hours[weekly_meeting_hours['duration_hours'] > 20]
    heavy_weeks_count = meeting_heavy_weeks.groupby('employee_id').size().reset_index(name='meeting_heavy_weeks')
    meeting_heavy_employees = heavy_weeks_count[heavy_weeks_count['meeting_heavy_weeks'] >= 2]
    result = pd.merge(meeting_heavy_employees, employees, on='employee_id', how='inner')
    result = result.sort_values(by=['meeting_heavy_weeks', 'employee_name'], ascending=[False, True])
    return result[['employee_id', 'employee_name', 'department', 'meeting_heavy_weeks']]
