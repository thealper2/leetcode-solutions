from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for num in encoded:
            result.append(num ^ result[-1])

        return result