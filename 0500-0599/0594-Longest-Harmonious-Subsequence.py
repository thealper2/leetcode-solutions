from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max((freq[num] + freq[num+1] for num in freq if num+1 in freq), default=0)
