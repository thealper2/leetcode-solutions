from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = []
        for i, num in enumerate(nums):
            if num == x:
                indices.append(i)

        result = []
        for query in queries:
            if query <= len(indices):
                result.append(indices[query - 1])
            else:
                result.append(-1)

        return result
