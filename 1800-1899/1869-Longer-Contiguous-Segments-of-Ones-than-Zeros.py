class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        n = len(s)
        max_0 = 0
        max_1 = 0
        current_1 = 0
        current_0 = 0

        for i in range(n):
            if s[i] == '1':
                current_0 = 0
                current_1 += 1
            else:
                current_0 += 1
                current_1 = 0

            max_0 = max(max_0, current_0)
            max_1 = max(max_1, current_1)

        return max_1 > max_0