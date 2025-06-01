from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = -1
        
        for i in range(n - 1):
            if nums[i + 1] - nums[i] != 1:
                continue
            
            current_len = 2
            expected_diff = -1
            
            for j in range(i + 1, n - 1):
                if nums[j + 1] - nums[j] == expected_diff:
                    current_len += 1
                    expected_diff *= -1
                else:
                    break
            
            if current_len > max_len:
                max_len = current_len
        
        return max_len