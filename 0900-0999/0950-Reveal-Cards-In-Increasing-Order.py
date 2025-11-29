from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = [0] * n
        idx = list(range(n))
        p = 0

        for card in deck:
            result[idx[p]] = card
            p += 1
            if p < len(idx):
                idx.append(idx[p])
                p += 1

        return result
