from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        stack = [(0, [])]
        
        while stack:
            start, path = stack.pop()
            
            if start == n:
                result.append(path)
                continue
                
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring == substring[::-1]:
                    stack.append((end, path + [substring]))
        
        return result
