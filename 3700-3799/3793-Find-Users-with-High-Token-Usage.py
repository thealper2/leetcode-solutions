import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    user_stats = prompts.groupby("user_id").agg(
        prompt_count=("prompt", "count"),
        avg_tokens=("tokens", "mean"),
    ).reset_index()

    user_stats = user_stats[user_stats["prompt_count"] >= 3].copy()

    def has_above_average(group):
        avg_tokens = group["tokens"].mean()
        return (group["tokens"] > avg_tokens).any()

    users_with_above_avg = prompts.groupby("user_id").filter(has_above_average)
    valid_user_ids = users_with_above_avg["user_id"].unique()
    user_stats = user_stats[user_stats["user_id"].isin(valid_user_ids)]

    user_stats["avg_tokens"] = user_stats["avg_tokens"].round(2)

    user_stats = user_stats.sort_values(["avg_tokens", "user_id"], ascending=[False, True])

    return user_stats[['user_id', 'prompt_count', 'avg_tokens']]
