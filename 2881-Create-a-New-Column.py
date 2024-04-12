import pandas as pd
from typing import List

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'].apply(lambda x: x * 2)
    return employees
