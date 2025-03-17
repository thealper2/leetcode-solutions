import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    if len(my_numbers.drop_duplicates(keep=False)) == 0:
        return pd.DataFrame({"num": [None]})
    else:
        return (
            my_numbers.drop_duplicates(keep=False)
            .sort_values(by="num", ascending=False)[:1]
            .reset_index(drop=True)
        )
