from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    if len(cost) == 0:
        return 0
    elif len(cost) == 1:
        return cost[0]

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):
        current = cost[i] + min(prev1, prev2)
        #print(i, current, '=', cost[i], min(prev1, prev2))
        prev2 = prev1
        prev1 = current

    return min(prev1, prev2)
