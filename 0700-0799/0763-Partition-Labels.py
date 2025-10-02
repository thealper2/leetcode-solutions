from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrences = {}
        for i, c in enumerate(s):
            last_occurrences[c] = i

        result = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last_occurrences[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
