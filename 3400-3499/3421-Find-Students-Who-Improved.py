import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    grouped = scores.sort_values(['student_id', 'subject', 'exam_date']).groupby(['student_id', 'subject'])
    result = grouped.agg(
        first_score=('score', 'first'),
        latest_score=('score', 'last'),
        exam_count=('score', 'count')
    ).reset_index()
    improved = result[(result['exam_count'] >= 2) & (result['latest_score'] > result['first_score'])]
    return improved[['student_id', 'subject', 'first_score', 'latest_score']].sort_values(['student_id', 'subject'])