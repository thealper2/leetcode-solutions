from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n = len(score)

        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if score[j][k] > score[max_idx][k]:
                    max_idx = j

            score[i], score[max_idx] = score[max_idx], score[i]
        
        return score
