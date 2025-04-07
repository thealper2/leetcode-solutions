from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            temp = i
            f = True
            while temp > 0:
                d = temp % 10
                temp //= 10
                if d == 0 or i % d != 0:
                    f = False

            if f:
                result.append(i)

        return result