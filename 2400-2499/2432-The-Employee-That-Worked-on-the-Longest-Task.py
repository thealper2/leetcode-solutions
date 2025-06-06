from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        n = len(logs)
        max_duration = -1
        max_employee = None

        for i in range(n):
            if i == 0:
                duration = logs[i][1] - 0
            else:
                duration = logs[i][1] - logs[i - 1][1]

            if duration > max_duration or (duration == max_duration and logs[i][0] < max_employee):
                max_duration = duration
                max_employee = logs[i][0]

        return max_employee