class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        curr = 'a'
        for char in word:
            c_pos = ord(curr) - ord('a')
            t_pos = ord(char) - ord('a')
            t1 = (t_pos - c_pos) % 26
            t2 = (c_pos - t_pos) % 26
            move = min(t1, t2)
            total += move + 1
            curr = char

        return total
