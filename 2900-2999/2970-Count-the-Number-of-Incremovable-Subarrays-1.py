from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_increasing(arr):
            if not arr:
                return True
                
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False

            return True

        n = len(nums)
        count = 0

        for start in range(n):
            for end in range(start + 1, n + 1):
                if is_increasing(nums[:start] + nums[end:]):
                    count += 1
    
        return count
