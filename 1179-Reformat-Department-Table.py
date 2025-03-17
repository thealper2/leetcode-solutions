import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    pivot = pd.pivot_table(
        data=department, index="id", columns="month", values="revenue"
    ).reindex(columns=months)
    pivot["id"] = pivot.index
    pivot = pivot.reset_index(drop=True)
    pivot = pivot.rename_axis(None, axis=1)
    cols = pivot.columns.tolist()
    cols.remove("id")
    cols = ["id"] + cols
    pivot.columns = ["id"] + [col + "_Revenue" for col in pivot.columns if col != "id"]
    return pivot
