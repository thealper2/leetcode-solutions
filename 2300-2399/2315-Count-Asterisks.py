class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside_pair = False
        for char in s:
            if char == '|':
                inside_pair = not inside_pair
            elif char == '*' and not inside_pair:
                count += 1
        return count