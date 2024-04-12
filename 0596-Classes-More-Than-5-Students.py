import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class', as_index=False).count()
    return courses[courses['student'] >= 5][['class']]
