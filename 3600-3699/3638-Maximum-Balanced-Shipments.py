from typing import List


class Solution:
    def maxBalancedShipments(self, weights: List[int]) -> int:
        max_weight = 0
        count = 0

        for weight in weights:
            if weight < max_weight:
                count += 1
                max_weight = 0

            else:
                max_weight = weight

        return count
