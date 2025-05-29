from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prev = 0
        max_duration = 0
        max_key = " "

        for i in range(len(releaseTimes)):
            duration = releaseTimes[i] - prev
            prev = releaseTimes[i]

            if duration > max_duration:
                max_duration = duration
                max_key = keysPressed[i]
            elif duration == max_duration:
                if keysPressed[i] > max_key:
                    max_key = keysPressed[i]

        return max_key
