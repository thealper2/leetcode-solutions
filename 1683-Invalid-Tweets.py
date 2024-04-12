def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda row: 0 if (row['name'].startswith('M')) or (row['employee_id'] % 2 == 0) else row['salary'], axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
