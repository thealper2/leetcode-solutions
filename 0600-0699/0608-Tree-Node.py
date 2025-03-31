import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["type"] = tree["p_id"].apply(lambda x: "Root" if pd.isna(x) else "Inner")
    if len(tree) > 1:
        has_children = tree["id"].isin(tree["p_id"].dropna())
        tree.loc[~has_children, "type"] = "Leaf"
    return tree[["id", "type"]]
