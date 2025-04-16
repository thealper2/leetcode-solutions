from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {}
        d2 = {}

        for word in words1:
            if word not in d1:
                d1[word] = 1
            else:
                d1[word] += 1

        for word in words2:
            if word not in d2:
                d2[word] = 1
            else:
                d2[word] += 1

        result = 0
        for word in d1:
            if d1[word] == 1 and word in d2 and d2[word] == 1:
                result += 1
        
        return result