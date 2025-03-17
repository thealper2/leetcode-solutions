import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    sorted = weather.sort_values(by="recordDate")
    return sorted[
        (sorted["temperature"] > sorted["temperature"].shift(1))
        & (sorted["recordDate"].diff().dt.days == 1)
    ][["id"]]
