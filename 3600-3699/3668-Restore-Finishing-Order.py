from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        for item in order:
            if item in friends:
                result.append(item)

        return result
