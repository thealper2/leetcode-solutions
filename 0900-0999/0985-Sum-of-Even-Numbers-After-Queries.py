from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        for num in nums:
            if num % 2 == 0:
                total += num
        
        result = []
        for query in queries:
            val, idx = query
            original_num = nums[idx]
            nums[idx] += val
            new_num = nums[idx]
            
            if original_num % 2 == 0:
                total -= original_num

            if new_num % 2 == 0:
                total += new_num
            
            result.append(total)
        
        return result

