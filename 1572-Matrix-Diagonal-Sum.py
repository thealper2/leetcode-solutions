from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    n = len(mat)
    # print(n)

    main_diagonal_sum = 0
    anti_diagonal_sum = 0

    for i in range(n):
        main_diagonal_sum += mat[i][i]
        anti_diagonal_sum += mat[i][n - 1 - i]

    if n % 2 == 1:
        main_diagonal_sum -= mat[int(n / 2)][int(n / 2)]

    return main_diagonal_sum + anti_diagonal_sum
