import pandas as pd


def movie_ratings(
    movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame
) -> pd.DataFrame:
    best_user = (
        movie_rating.groupby(["user_id"], as_index=False)["movie_id"]
        .count()
        .merge(users, on="user_id", how="left")
        .sort_values(["movie_id", "name"], ascending=[False, True])["name"]
        .values[0]
    )
    movie_rating = movie_rating[
        movie_rating["created_at"].dt.to_period("M") == "2020-02"
    ]
    best_movie = (
        movie_rating.groupby(["movie_id"], as_index=False)["rating"]
        .mean()
        .merge(movies, on="movie_id", how="left")
        .sort_values(["rating", "title"], ascending=[False, True])["title"]
        .values[0]
    )
    return pd.DataFrame({"results": [best_user, best_movie]})
