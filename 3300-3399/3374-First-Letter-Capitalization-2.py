import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content["converted_text"] = user_content["content_text"].apply(
        lambda x: " ".join(['-'.join([c.capitalize() for c in word.split('-')]) for word in x.split()])
    )
    user_content.rename(columns={"content_text": "original_text"}, inplace=True)
    return user_content