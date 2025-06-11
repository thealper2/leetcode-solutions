from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        stack = [(nums, [])]
        result = []
        
        while stack:
            current, path = stack.pop()
            n = len(current)
            if not current:
                result.append(path)
            else:
                for i in range(n):
                    remaining = current[:i] + current[i+1:]
                    stack.append((remaining, path + [current[i]]))
        
        return result
