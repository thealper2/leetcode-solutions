from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            t = []
            parts = word.split(separator)
            for part in parts:
                if part:
                    t.append(part)

            result.extend(t)

        return result