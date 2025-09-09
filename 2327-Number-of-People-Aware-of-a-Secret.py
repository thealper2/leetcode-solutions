class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        for day in range(2, n + 1):
            for prev in range(1, day):
                if day - prev >= delay and day - prev < forget:
                    dp[day] = (dp[day] + dp[prev]) % MOD

            if day <= forget:
                dp[day] = (dp[day] + 1) % MOD

        return dp[n]
