import pandas as pd


def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(sales, products, on='product_id', how='left')
    merged['month'] = merged['sale_date'].dt.month
    merged['season'] = merged['month'].apply(
        lambda x: 'Winter' if x in [12, 1, 2] else
                  'Spring' if x in [3, 4, 5] else
                  'Summer' if x in [6, 7, 8] else 'Fall'
    )
    merged['revenue'] = merged['quantity'] * merged['price']
    season_category_stats = merged.groupby(['season', 'category']).agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('revenue', 'sum')
    ).reset_index()
    most_popular = season_category_stats.loc[
        season_category_stats.groupby('season')['total_quantity'].idxmax()
    ]
    most_popular = season_category_stats.sort_values(
        by=['season', 'total_quantity', 'total_revenue'],
        ascending=[True, False, False]
    ).drop_duplicates('season', keep='first')
    result = most_popular[['season', 'category', 'total_quantity', 'total_revenue']].sort_values('season')
    return result
