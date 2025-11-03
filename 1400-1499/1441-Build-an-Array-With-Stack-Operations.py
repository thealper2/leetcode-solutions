from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        stream_num = 1
        i = 0
        while i < len(target) and stream_num <= n:
            operations.append('Push')
            if stream_num == target[i]:
                i += 1
            else:
                operations.append('Pop')

            stream_num += 1

        return operations
