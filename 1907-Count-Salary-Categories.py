import numpy as np
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['Low Salary'] = np.where(accounts['income'] < 20000, 1, 0)
    accounts['Average Salary'] = np.where((accounts['income'] >= 20000) & (accounts['income'] <= 50000), 1, 0)
    accounts['High Salary'] = np.where((accounts['income'] > 50000), 1, 0)
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [accounts['Low Salary'].sum(), accounts['Average Salary'].sum(), accounts['High Salary'].sum()]
    })
