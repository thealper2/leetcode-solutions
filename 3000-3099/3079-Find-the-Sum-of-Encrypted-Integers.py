from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            m = 0
            c = 0
            while num > 0:
                i = num % 10
                if i > m:
                    m = i

                num //= 10
                c += 1

            while c > 0:
                c -= 1
                result += (10 ** c) * m

        return result