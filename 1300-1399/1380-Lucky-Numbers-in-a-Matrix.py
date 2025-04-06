from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []
        rows = len(matrix)

        for i in range(rows):
            min_in_row = min(matrix[i])
            col_index = matrix[i].index(min_in_row)
            max_in_col = col_index
            for j in range(rows):
                if matrix[j][col_index] > max_in_col:
                    max_in_col = matrix[j][col_index]

            if max_in_col == min_in_row:
                lucky_numbers.append(max_in_col)

        return lucky_numbers