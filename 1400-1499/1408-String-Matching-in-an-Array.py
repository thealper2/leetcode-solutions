from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        found = set()
        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[i] in words[j]:
                        if words[i] not in found:
                            found.add(words[i])
                            break
                    
        return list(found)