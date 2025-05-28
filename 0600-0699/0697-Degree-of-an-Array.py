from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occurence = {}
        last_occurence = {}

        for idx, num in enumerate(nums):
            if num not in first_occurence:
                first_occurence[num] = idx

            last_occurence[num] = idx
            count[num] += 1

        degree = max(count.values())

        min_length = float('inf')
        for num in count.keys():
            if count[num] == degree:
                length = last_occurence[num] - first_occurence[num] + 1
                if length < min_length:
                    min_length = length

        return min_length