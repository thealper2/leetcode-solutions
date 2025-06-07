import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    current_borrowings = borrowing_records[borrowing_records['return_date'].isna()]
    borrow_counts = current_borrowings['book_id'].value_counts().reset_index()
    borrow_counts.columns = ['book_id', 'current_borrowers']
    merged = library_books.merge(borrow_counts, on='book_id', how='inner')
    result = merged[merged['total_copies'] == merged['current_borrowers']]
    result = result.sort_values(['current_borrowers', 'title'], ascending=[False, True])
    return result[['book_id', 'title', 'author', 'genre', 'publication_year', 'current_borrowers']]