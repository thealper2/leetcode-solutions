import pandas as pd
from typing import List

def createDataframe(student_data) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df