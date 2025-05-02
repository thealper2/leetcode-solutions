class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[i:i+k] for i in range(0, len(s), k)]
            new_s = []
            for group in groups:
                digit_sum = sum(int(d) for d in group)
                new_s.append(str(digit_sum))

            s = ''.join(new_s)

        return s