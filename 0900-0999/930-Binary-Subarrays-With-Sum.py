from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        current_sum = 0
        cnt = 0

        for num in nums:
            current_sum += num
            cnt += prefix_sum_count.get(current_sum - goal, 0)
            prefix_sum_count[current_sum] += 1

        return cnt
