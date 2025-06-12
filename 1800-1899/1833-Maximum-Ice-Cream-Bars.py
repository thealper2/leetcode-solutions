from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        min_val = min(costs)
        max_val = max(costs)

        count_range = max_val - min_val + 1
        count = [0] * count_range
        output = [0] * len(costs)

        for cost in costs:
            count[cost - min_val] += 1

        for i in range(1, count_range):
            count[i] += count[i - 1]

        for cost in reversed(costs):
            count[cost - min_val] -= 1
            output[count[cost - min_val]] = cost

        result = 0
        for i in range(len(costs)):
            if output[i] <= coins:
                coins -= output[i]
                result += 1
            else:
                return result

        return result
