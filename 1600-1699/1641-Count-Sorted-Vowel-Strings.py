class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n-1):
            o += u
            i += o
            e += i
            a += e
            
        return a + e + i + o + u
