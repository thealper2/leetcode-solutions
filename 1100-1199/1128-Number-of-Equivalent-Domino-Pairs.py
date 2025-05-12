from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = {}
        m = 0
        for domino in dominoes:
            if domino[0] > domino[1]:
                domino[0], domino[1] = domino[1], domino[0]
            
            key = str(domino[0]) + "-" + str(domino[1])
            count = result.get(key, 0)
            count += 1
            result[key] = count
            m += count - 1

        return m