import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee.sort_values(by='salary', ascending=False)[['salary']]
    if N <= salaries['salary'].nunique() and N > 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [salaries['salary'].unique()[N-1]]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
