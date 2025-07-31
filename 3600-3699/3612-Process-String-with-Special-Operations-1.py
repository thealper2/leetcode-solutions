class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for c in s:
            if 97 <= ord(c) <= 122:
                result += c
            elif c == '*':
                result = result[:-1]
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]

        return result
