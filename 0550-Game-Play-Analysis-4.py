import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first_date"] = activity.groupby(by=["player_id"], as_index=False)[["event_date"]].transform("min")
    grouped = activity[(activity['event_date'] - activity['first_date']).dt.total_seconds() == 86400]
    return pd.DataFrame({"fraction":[round(grouped.player_id.nunique() / activity.player_id.nunique(), 2)]})
