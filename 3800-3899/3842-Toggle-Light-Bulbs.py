from collections import Counter

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        freq = Counter(bulbs)
        result = []
        for k in sorted(freq.keys()):
            if freq[k] % 2:
                result.append(k)
            
        if not result:
            return []

        return result
