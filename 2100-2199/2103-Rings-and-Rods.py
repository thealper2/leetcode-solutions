class Solution:
    def countPoints(self, rings: str) -> int:
        stack = [""] * 10
        count = 0

        for i in range(0, len(rings), 2):
            idx, letter = int(rings[i+1]), rings[i]
            stack[idx] += letter

        for item in stack:
            if ("R" in item) and ("G" in item) and ("B" in item):
                count += 1

        return count