from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0
        for seat, student in zip(seats, students):
            result += abs(seat - student)

        return result