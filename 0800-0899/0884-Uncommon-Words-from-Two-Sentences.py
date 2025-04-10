from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        d = {}
        result = []

        for s in s1:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for s in s2:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for k, v in d.items():
            if v == 1:
                result.append(k)

        return result