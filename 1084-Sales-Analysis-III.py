import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    start_date = '2019-01-01'
    end_date = '2019-03-31'
    merged_df = pd.merge(sales, product, on='product_id')
    first_quarter_sales = merged_df[(merged_df['sale_date'] >= start_date) & (merged_df['sale_date'] <= end_date)]
    all_sales_grouped = merged_df.groupby('product_id')['sale_date'].agg(['min', 'max']).reset_index()
    only_first_quarter_products = all_sales_grouped[(all_sales_grouped['min'] >= start_date) & (all_sales_grouped['max'] <= end_date)]
    result = pd.merge(only_first_quarter_products[['product_id']], product[['product_id', 'product_name']], on='product_id')
    return result