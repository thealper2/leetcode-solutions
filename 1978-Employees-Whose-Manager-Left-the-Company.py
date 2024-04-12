import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees[~employees['manager_id'].isin(employees['employee_id'])]
    employees = employees[employees['salary'] < 30000]
    employees = employees[employees['manager_id'].notnull()]
    return employees.sort_values(by='employee_id', ascending=True)[['employee_id']]
