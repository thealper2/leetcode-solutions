from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        result = []
        e_ptr = o_ptr = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[e_ptr])
                e_ptr += 1
            else:
                result.append(odd[o_ptr])
                o_ptr += 1
                
        return result