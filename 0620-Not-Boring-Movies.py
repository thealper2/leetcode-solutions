import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema.index % 2 == 0) & (cinema['description'] != 'boring')].sort_values(by='rating', ascending=False).reset_index(drop=True)
