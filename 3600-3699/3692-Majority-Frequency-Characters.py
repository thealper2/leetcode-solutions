from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)
        groups = defaultdict(list)
        for c, f in freq.items():
            groups[f].append(c)

        best_size = -1
        best_freq = -1
        best_group = []

        for f, chars in groups.items():
            size = len(chars)
            if size > best_size or (size == best_size and f > best_freq):
                best_size = size
                best_freq = f
                best_group = chars

        return ''.join(best_group)
