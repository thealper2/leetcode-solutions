from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c = 0
        n = len(startTime)
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                c += 1
        return c