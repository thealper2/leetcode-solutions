from collections import defaultdict


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = defaultdict(int)
        for c in word:
            counts[c] += 1

        if len(set(counts.values())) > 2:
            return False

        count_keys = list(counts.keys())
        for c in count_keys:
            counts[c] -= 1
            if counts[c] == 0:
                del counts[c]

            if len(set(counts.values())) == 1:
                return True

            counts[c] += 1

        return False
