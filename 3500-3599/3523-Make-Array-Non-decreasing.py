from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            while stack and num < stack[-1]:
                num = max(stack.pop(), num)

            stack.append(num)

        return len(stack)
