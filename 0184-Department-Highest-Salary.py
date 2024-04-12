import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salaries = employee.groupby('departmentId')['salary'].max()
    result = employee[employee.apply(lambda row: row['salary'] == max_salaries[row['departmentId']], axis=1)]
    result = pd.merge(result, department, left_on='departmentId', right_on='id', how='inner')[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    return result
