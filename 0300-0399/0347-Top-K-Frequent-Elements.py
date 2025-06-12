from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for d in nums:
            freq[d] += 1
        
        max_freq = max(freq.values()) if freq else 0
        buckets = [[] for _ in range(max_freq + 1)]
        
        for char, count in freq.items():
            buckets[count].append(char)

        result = []
        for count in range(max_freq, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
