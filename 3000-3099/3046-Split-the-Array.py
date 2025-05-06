from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                if count[num] > 2:
                    return False
                
        return True