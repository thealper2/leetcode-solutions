from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        max_lucky = -1
        for num, count in d.items():
            if num == count and num > max_lucky:
                max_lucky = num
                
        return max_lucky