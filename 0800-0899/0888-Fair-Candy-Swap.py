from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        delta = (sum_alice - sum_bob) // 2
        alice_set = set(aliceSizes)

        for b in bobSizes:
            a = b + delta
            if a in alice_set:
                return [a, b]
            
        return []