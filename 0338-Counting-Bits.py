class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            temp = []
            while i >= 1:
                temp.append(i % 2)
                i = i // 2

            result.append(sum(temp))

        return result


#################


class Solution2:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2

            dp[i] = 1 + dp[i - offset]

        return dp
