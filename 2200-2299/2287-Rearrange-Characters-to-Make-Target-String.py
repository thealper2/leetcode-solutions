from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        target_count = Counter(target)
        
        max_string = float('inf')

        for c in target_count:
            max_string = min(max_string, s_count[c] // target_count[c])

        return max_string