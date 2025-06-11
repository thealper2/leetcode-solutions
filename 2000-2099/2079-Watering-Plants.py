from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        current_capacity = capacity

        for i in range(n):
            if plants[i] > current_capacity:
                steps += 2 * i
                current_capacity = capacity
            
            steps += 1
            current_capacity -= plants[i]
        
        return steps
