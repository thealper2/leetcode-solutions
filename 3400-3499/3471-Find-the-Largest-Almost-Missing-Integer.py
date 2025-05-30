from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarrays = [nums[i:i+k] for i in range(n - k + 1)]
        
        count = defaultdict(int)
        for subarray in subarrays:
            unique_in_subarray = set(subarray)
            for num in unique_in_subarray:
                count[num] += 1
        
        max_result = -1
        for num, cnt in count.items():
            if cnt == 1 and num > max_result:
                max_result = num
        
        return max_result
