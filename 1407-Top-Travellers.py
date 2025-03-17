import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(users, rides, how="left", left_on="id", right_on="user_id")
    merged_df["distance"] = merged_df["distance"].fillna(0)
    result = merged_df.groupby(["id_x", "name"], as_index=False)["distance"].sum()
    result = result.sort_values(by=["distance", "name"], ascending=[False, True])
    result = result.rename(columns={"distance": "travelled_distance"}).reset_index(
        drop=True
    )
    return result[["name", "travelled_distance"]]
