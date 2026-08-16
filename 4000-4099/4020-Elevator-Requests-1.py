class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current_floor = 0
        total = 0

        for floor in requests:
            total += abs(current_floor - floor)
            current_floor = floor

        return total