import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks["state"] = stocks["operation"].map({"Buy": -1, "Sell": 1})
    stocks["price"] = (stocks["state"] * stocks["price"]).astype(float)
    result = stocks.groupby("stock_name", as_index=False)["price"].sum()
    result.price = result.price.astype(int)
    result.columns = ["stock_name", "capital_gain_loss"]
    return result
