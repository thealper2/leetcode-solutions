from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        n = len(code)
        code.extend(code)
        if k > 0:
            for i in range(n):
                result.append(sum(code[i+1:i+1+k]))
        elif k < 0:
            for i in range(n):
                result.append(sum(code[n+k+i:n+i]))
        else:
            result = [0] * n

        return result