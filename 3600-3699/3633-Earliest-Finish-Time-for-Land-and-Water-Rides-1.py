from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_time = float('inf')
    
        for i in range(len(landStartTime)):
            land_start = landStartTime[i]
            land_end = land_start + landDuration[i]
            for j in range(len(waterStartTime)):
                water_start = max(waterStartTime[j], land_end)
                water_end = water_start + waterDuration[j]
                if water_end < min_time:
                    min_time = water_end
        
        for j in range(len(waterStartTime)):
            water_start = waterStartTime[j]
            water_end = water_start + waterDuration[j]
            for i in range(len(landStartTime)):
                land_start = max(landStartTime[i], water_end)
                land_end = land_start + landDuration[i]
                if land_end < min_time:
                    min_time = land_end
        
        return min_time
