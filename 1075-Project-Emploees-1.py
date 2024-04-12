import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(project, employee, on='employee_id', how='inner')
    return merged[['project_id', 'experience_years']].groupby(by='project_id', as_index=False).mean().round(2).rename(columns={'experience_years': 'average_years'})
