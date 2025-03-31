import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs["var"] = logs["num"].rolling(window=3).var()
    return (
        logs[logs["var"] == 0][["num"]]
        .drop_duplicates(keep="first")
        .rename(columns={"num": "ConsecutiveNums"})
    )
