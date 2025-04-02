from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0

        for floor in bank:
            current = floor.count('1')
            if current == 0:
                continue

            result += prev * current
            prev = current

        return result