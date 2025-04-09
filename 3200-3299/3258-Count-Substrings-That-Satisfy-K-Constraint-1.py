class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total = 0
        left = 0
        count_0 = 0
        count_1 = 0

        for right in range(n):
            if s[right] == '0':
                count_0 += 1
            else:
                count_1 += 1

            while count_0 > k and count_1 > k:
                if s[left] == '0':
                    count_0 -= 1
                else:
                    count_1 -= 1
                left += 1

            total += (right - left + 1)

        return total