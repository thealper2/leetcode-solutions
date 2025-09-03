class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        black_positions = [i for i, char in enumerate(s) if char == '1']
        total_black = len(black_positions)
        if total_black == 0:
            return 0

        target_positions = list(range(n - total_black, n))
        steps = 0
        for i in range(total_black):
            steps += abs(black_positions[i] - target_positions[i])

        return steps
