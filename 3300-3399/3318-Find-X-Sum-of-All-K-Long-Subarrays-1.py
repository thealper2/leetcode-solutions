from collections import defaultdict
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = defaultdict(int)
            for num in window:
                freq[num] += 1
            
            freq_list = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            top_elements = [item[0] for item in freq_list[:x]]
            
            x_sum = 0
            for num in top_elements:
                x_sum += num * freq[num]
            
            answer.append(x_sum)
        
        return answer