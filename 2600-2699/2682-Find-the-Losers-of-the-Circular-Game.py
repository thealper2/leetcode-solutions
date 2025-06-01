from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = [0] * n
        idx = 0
        initial_k = k

        while True:
            players[idx] = 1
            next_idx = (idx + k) % n
            k += initial_k

            if players[next_idx] == 1:
                break

            idx = next_idx

        return [i + 1 for i in range(n) if players[i] == 0]