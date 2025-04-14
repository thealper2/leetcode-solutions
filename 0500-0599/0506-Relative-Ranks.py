from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = [""] * n
        
        for i in range(n):
            count = 0
            for j in range(n):
                if score[j] > score[i]:
                    count += 1
            if count == 0:
                ranks[i] = "Gold Medal"
            elif count == 1:
                ranks[i] = "Silver Medal"
            elif count == 2:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(count + 1)
        
        return ranks