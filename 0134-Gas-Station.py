from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(cost) > sum(gas):
        return -1

    tank, res = 0, 0

    for i in range(len(gas)):
        tank += (gas[i] - cost[i])
        print(i, tank)

        if tank < 0:
            tank = 0
            res = i + 1
    return res
