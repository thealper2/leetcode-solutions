import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    consecutive_mask = (
        stadium['people'].rolling(window=3, min_periods=1)
        .apply(lambda x: all(x >= 100) if len(x) == 3 else False)
        .astype(bool)
    )
    
    result_mask = consecutive_mask | consecutive_mask.shift(-1) | consecutive_mask.shift(-2)
    return stadium[result_mask].reset_index(drop=True)