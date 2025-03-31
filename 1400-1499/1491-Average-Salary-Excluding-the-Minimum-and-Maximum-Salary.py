def average(salary: List[int]) -> float:
    min_salary, max_salary = sorted(salary)[0], sorted(salary)[-1]
    while salary.count(min_salary) > 0 or salary.count(max_salary) > 0:
        salary.remove(min_salary)
        salary.remove(max_salary)

    print(min_salary, max_salary)
    return float("%.5f" % (sum(salary) / len(salary)))
