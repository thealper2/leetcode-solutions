import pandas as pd


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return np.floor(n * multiplier + 0.5) / multiplier

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    df = (
        reading_sessions
        .groupby("book_id", as_index=False)
        .agg(
            total=("session_rating", "count"),
            max_rating=("session_rating", "max"),
            min_rating=("session_rating", "min"),
            extreme_count=("session_rating", lambda x: ((x <= 2) | (x >= 4)).sum())
        )
        .assign(
            rating_spread=lambda df: df.max_rating - df.min_rating,
            polarization_score=lambda df: round_half_up(df.extreme_count / df.total, 2)
        )
        .query("max_rating >= 4 and min_rating <= 2 and total >= 5 and polarization_score >= 0.6")
        .drop(columns=["total", "max_rating", "min_rating", "extreme_count"])
        .merge(books, on="book_id", how="inner")
        .sort_values(by=["polarization_score", "title"], ascending=[False, False])
        .reset_index(drop=True)
    )
    return df[['book_id', 'title', 'author', 'genre', 'pages', 'rating_spread', 'polarization_score']]
