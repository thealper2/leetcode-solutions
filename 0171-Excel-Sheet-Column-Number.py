class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for i in range(len(columnTitle)):
            hex_str = ord(columnTitle[i]) - 64
            count += hex_str * (26 ** (len(columnTitle) - i - 1))

        return count