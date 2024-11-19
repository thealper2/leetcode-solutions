class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        p_a = 0
        p_b = len(s) - 1
        vowels = set("aeiouAEIOU")

        while p_a < p_b:
            if s[p_a] not in vowels:
                p_a += 1
            elif s[p_b] not in vowels:
                p_b -= 1
            else:
                temp = s[p_a]
                s[p_a] = s[p_b]
                s[p_b] = temp
                p_a += 1
                p_b -= 1

        return "".join(s)