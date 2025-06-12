class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [_ for _ in range(1, n + 1)]
        visited = set()
        idx = 0

        while len(friends) > 1:
            idx = (idx + k - 1) % len(friends)
            friends.pop(idx)

        return friends[0]
