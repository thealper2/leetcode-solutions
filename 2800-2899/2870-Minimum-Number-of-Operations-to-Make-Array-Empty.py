from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        total_operations = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            operations_3 = count // 3
            remainder = count % 3
            if remainder == 0:
                total_operations += operations_3
            else:
                if remainder == 1:
                    if operations_3 >= 1:
                        total_operations += (operations_3 - 1) + 2
                    else:
                        return -1
                elif remainder == 2:
                    total_operations += operations_3 + 1
        
        return total_operations
