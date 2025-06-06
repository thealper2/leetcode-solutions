from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        x = len(flowerbed)
        for i in range(x):
            if flowerbed[i] == 0:
                if ((i == 0) or (flowerbed[i - 1] == 0)) and ((i == x - 1) or (flowerbed[i + 1] == 0)):
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n
