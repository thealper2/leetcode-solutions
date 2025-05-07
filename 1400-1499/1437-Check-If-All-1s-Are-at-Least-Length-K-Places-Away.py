from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                if last == None:
                    last = i
                    continue
                
                if i - last - 1 < k:
                    return False
                
                last = i

        return True
