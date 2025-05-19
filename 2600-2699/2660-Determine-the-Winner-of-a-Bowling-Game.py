from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        p1 = 0
        p2 = 0
        i = 0

        while (i < n):
            if (i >= 1 and player1[i - 1] == 10) or (i >= 2 and player1[i - 2] == 10):
                p1 += 2 * player1[i]
            else:
                p1 += player1[i]

            if (i >= 1 and player2[i - 1] == 10) or (i >= 2 and player2[i - 2] == 10):
                p2 += 2 * player2[i]
            else:
                p2 += player2[i]

            i += 1

        if (p1 > p2):
            return 1
        elif (p1 < p2):
            return 2

        return 0