import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(users, register, on="user_id", how="left")[
        ["contest_id", "user_id"]
    ]
    merged = merged.groupby(by="contest_id", as_index=False).count()
    merged["percentage"] = (merged["user_id"] / users["user_id"].nunique()).round(
        4
    ) * 100
    merged = merged.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True]
    )[["contest_id", "percentage"]]
    return merged
