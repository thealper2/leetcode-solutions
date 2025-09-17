from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        char_sets = [set(word) for word in words]
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not char_sets[i] & char_sets[j]:
                    max_prod = max(
                        max_prod,
                        len(words[i]) * len(words[j])
                    )

        return max_prod
