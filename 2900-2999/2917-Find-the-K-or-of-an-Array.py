from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for num in nums:
            i = 0
            while num > 0:
                d = num % 2
                num //= 2
                
                if d == 1:
                    if i not in num_dict:
                        num_dict[i] = 1
                    else:
                        num_dict[i] += 1

                i += 1

        result = 0
        for a, b in num_dict.items():
            if k <= b:
                result += 2 ** a

        return result