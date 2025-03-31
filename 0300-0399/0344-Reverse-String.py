class Solution:
    def reverseString(self, s: List[str]) -> None:
        p_a = 0
        p_b = len(s) - 1

        while p_a <= p_b:
            temp = s[p_a]
            s[p_a] = s[p_b]
            s[p_b] = temp

            p_a += 1
            p_b -= 1

        return s
