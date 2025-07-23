import pandas as pd


def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    reviews_sorted = performance_reviews.sort_values(['employee_id', 'review_date'], ascending=[True, False])
    last_three_reviews = reviews_sorted.groupby('employee_id').head(3)
    review_counts = last_three_reviews.groupby('employee_id').size()
    valid_employees = review_counts[review_counts == 3].index
    last_three_reviews = last_three_reviews[last_three_reviews['employee_id'].isin(valid_employees)]

    def is_increasing(group):
        sorted_group = group.sort_values('review_date')
        ratings = sorted_group['rating'].values
        return all(ratings[i] < ratings[i + 1] for i in range(len(ratings) - 1))

    increasing_ratings = last_three_reviews.groupby('employee_id').apply(is_increasing)
    improving_employees = increasing_ratings[increasing_ratings].index

    def calculate_improvement(group):
        sorted_group = group.sort_values('review_date')
        return sorted_group['rating'].iloc[-1] - sorted_group['rating'].iloc[0]

    improvement_scores = last_three_reviews.groupby('employee_id').apply(calculate_improvement)
    improvement_scores = improvement_scores[improvement_scores.index.isin(improving_employees)]

    result = pd.merge(
        improvement_scores.reset_index(),
        employees,
        on='employee_id'
    )
    result.columns = ['employee_id', 'improvement_score', 'name']
    result = result.sort_values(['improvement_score', 'name'], ascending=[False, True])
    return result[['employee_id', 'name', 'improvement_score']]
