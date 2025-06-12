from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        max_freq = max(freq.values()) if freq else 0
        buckets = [[] for _ in range(max_freq + 1)]
        
        for char, count in freq.items():
            buckets[count].append(char)
        
        result = []
        for count in range(max_freq, 0, -1):
            for char in buckets[count]:
                result.append(char * count)
        
        return ''.join(result)
