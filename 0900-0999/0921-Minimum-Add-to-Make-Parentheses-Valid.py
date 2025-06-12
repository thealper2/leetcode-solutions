class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        required = 0

        for p in s:
            if p == '(':
                opened += 1
            else:
                if opened:
                    opened -= 1
                else:
                    required += 1

        return required + opened
