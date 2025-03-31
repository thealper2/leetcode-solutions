import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z0-9_]+@[A-Za-z]+\.com$'
    
    valid_users = users[
        users['email'].str.match(pattern, na=False)
    ].sort_values('user_id')
    
    return valid_users