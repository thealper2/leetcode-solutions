from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        current_length = 0
        prev_parity = None
        
        for num in nums:
            if num > threshold:
                current_length = 0
                prev_parity = None
                continue
                
            current_parity = num % 2
            
            if current_length == 0:
                if num % 2 == 0:
                    current_length = 1
                    prev_parity = current_parity
                    max_length = max(max_length, current_length)
                continue
                
            if current_parity != prev_parity:
                current_length += 1
                prev_parity = current_parity
                max_length = max(max_length, current_length)
            else:
                current_length = 1 if num % 2 == 0 else 0
                prev_parity = current_parity if num % 2 == 0 else None
        
        return max_length