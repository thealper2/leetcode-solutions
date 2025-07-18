import pandas as pd


def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    merged = product_purchases.merge(product_purchases, on='user_id', suffixes=('_1', '_2'))
    filtered = merged[merged['product_id_1'] < merged['product_id_2']]
    grouped = filtered.groupby(['product_id_1', 'product_id_2']).agg(
        customer_count=('user_id', 'nunique')
    ).reset_index()
    result = grouped[grouped['customer_count'] >= 3]
    result = result.merge(
        product_info[['product_id', 'category']],
        left_on='product_id_1',
        right_on='product_id',
        how='left'
    ).rename(columns={'category': 'product1_category'}).drop(columns=['product_id'])
    result = result.merge(
        product_info[['product_id', 'category']],
        left_on='product_id_2',
        right_on='product_id',
        how='left'
    ).rename(columns={'category': 'product2_category'}).drop(columns=['product_id'])
    result = result.sort_values(
        by=['customer_count', 'product_id_1', 'product_id_2'],
        ascending=[False, True, True]
    )
    result = result.rename(columns={
        'product_id_1': 'product1_id',
        'product_id_2': 'product2_id'
    })
    result = result[['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']]
    return result
