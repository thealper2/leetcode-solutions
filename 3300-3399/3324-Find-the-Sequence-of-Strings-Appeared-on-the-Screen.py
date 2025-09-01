from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        s = ""
        for char in target:
            s += "a"
            result.append(s)

            while s[-1] != char:
                last = chr(((ord(s[-1]) - ord('a') + 1) % 26) + ord('a'))
                s = s[:-1] + last
                result.append(s)

        return result
