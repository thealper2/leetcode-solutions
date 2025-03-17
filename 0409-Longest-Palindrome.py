class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        result = 0

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

            if d[char] % 2 == 0:
                result += 2

        for count in d.values():
            if count % 2 == 1:
                result += 1
                break

        return result
