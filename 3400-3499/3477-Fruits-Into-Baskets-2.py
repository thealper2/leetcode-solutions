from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        count = 0
        
        for i in range(n):
            placed = False
            for j in range(m):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    placed = True
                    break

            if not placed:
                count += 1

        return count
