class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        balance = 0
        idx = 0

        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                primitive = s[idx:i + 1]
                if len(primitive) >= 2:
                    result += primitive[1:-1]

                idx = i + 1

        return result