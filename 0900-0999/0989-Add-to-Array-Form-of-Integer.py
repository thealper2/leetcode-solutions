from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        n = len(num) - 1
        carry = 0

        while k > 0 or n >= 0 or carry > 0:
            sum_nk = carry
            if k > 0:
                sum_nk += k % 10
                k //= 10

            if n >= 0:
                sum_nk += num[n]
                n -= 1

            carry = sum_nk // 10
            result.append(sum_nk % 10)

        return result[::-1]
        
