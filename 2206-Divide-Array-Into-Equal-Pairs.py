from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        result = []
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.append(num)

        return len(result) == 0