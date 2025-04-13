from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            left, right = 0, len(mat[i])

            while left < right:
                mid = (left + right) // 2
                if mat[i][mid]== 1:
                    left = mid + 1
                else:
                    right = mid
                
            count = left
            rows.append((count, i))

        for i in range(len(rows)):
            min_idx = i
            for j in range(i+1, len(rows)):
                if rows[j][0] < rows[min_idx][0] or (rows[j][0] == rows[min_idx][0] and rows[j][1] < rows[min_idx][1]):
                    min_idx = j
            rows[i], rows[min_idx] = rows[min_idx], rows[i]
        
        result = [row[1] for row in rows[:k]]
        return result