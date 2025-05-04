from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        result = []
        count = 0
        
        for num in nums:
            if num != -1:
                seen.insert(0, num)
                count = 0
            else:
                count += 1
                if count <= len(seen):
                    result.append(seen[count - 1])
                else:
                    result.append(-1)
        
        return result