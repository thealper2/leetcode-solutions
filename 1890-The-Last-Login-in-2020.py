import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    result = logins[logins['time_stamp'].dt.year == 2020]
    result = result.groupby("user_id")["time_stamp"].max().reset_index()
    result = result.sort_values(by="user_id").reset_index(drop=True)
    result = result.rename(columns={"time_stamp": "last_stamp"})
    return result