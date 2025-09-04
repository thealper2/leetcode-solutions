from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        positions = set(nums)
        moves = len(moveFrom)
        for i in range(moves):
            if moveFrom[i] in positions:
                positions.remove(moveFrom[i])
                positions.add(moveTo[i])
        
        return sorted(positions)
