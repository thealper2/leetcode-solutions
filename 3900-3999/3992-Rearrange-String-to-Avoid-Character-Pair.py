from collections import Counter

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        counts = Counter(s)
        result = []
        result.append(y * counts.get(y, 0))
        for char in sorted(counts.keys()):
            if char != x and char != y:
                result.append(char * counts[char])

        result.append(x * counts.get(x, 0))
        return ''.join(result)
