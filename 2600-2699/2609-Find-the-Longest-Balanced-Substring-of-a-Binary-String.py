class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        temp = '01'
        found = False
        result = 0
        while not found:
            if temp in s:
                result += 2
                temp = '0' + temp + '1'
            else:
                found = True

        return result