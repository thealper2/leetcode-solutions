from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if "+" in operation:
                count += 1
            else:
                count -= 1

        return count