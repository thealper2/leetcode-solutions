from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        total = 0
        remaining = truckSize
        for boxes, units in boxTypes:
            if remaining <= 0:
                break
            
            take = min(boxes, remaining)
            total += take * units
            remaining -= take
        return total