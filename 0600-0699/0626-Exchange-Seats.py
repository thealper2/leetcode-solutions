import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, len(seat) - 1, 2):
        seat.loc[i : i + 1, "student"] = (
            seat.loc[i : i + 1, "student"].iloc[::-1].tolist()
        )

    return seat
