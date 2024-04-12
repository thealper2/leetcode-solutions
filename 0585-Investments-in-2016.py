import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    return insurance.drop_duplicates(subset=['lat', 'lon'], keep=False).loc[insurance.duplicated(subset='tiv_2015', keep=False)][['tiv_2016']].sum().round(2).to_frame('tiv_2016').reset_index(drop=True)
