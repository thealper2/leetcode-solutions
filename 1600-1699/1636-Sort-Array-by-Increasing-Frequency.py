from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        num_freq = [(num, freq) for num, freq in d.items()]
        
        n = len(num_freq)
        for i in range(n):
            for j in range(0, n-i-1):
                if num_freq[j][1] > num_freq[j+1][1]:
                    num_freq[j], num_freq[j+1] = num_freq[j+1], num_freq[j]
                elif num_freq[j][1] == num_freq[j+1][1]:
                    if num_freq[j][0] < num_freq[j+1][0]:
                        num_freq[j], num_freq[j+1] = num_freq[j+1], num_freq[j]
        
        sorted_nums = []
        for num, freq in num_freq:
            sorted_nums.extend([num] * freq)
        
        return sorted_nums