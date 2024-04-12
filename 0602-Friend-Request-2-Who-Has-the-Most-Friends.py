import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']]).value_counts().reset_index(name='num').rename(columns={'index': 'id'}).head(1)
