from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_val = -1
            max_index = -1

            for i in range(len(gifts)):
                if gifts[i] > max_val:
                    max_val = gifts[i]
                    max_index = i

            if max_val == 0:
                break

            gifts[max_index] = int(max_val ** 0.5)

        return sum(gifts)