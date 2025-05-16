class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_distance = 0
        consumed = 0

        while mainTank > 0:
            mainTank -= 1
            total_distance += 10
            consumed += 1

            if consumed % 5 == 0 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        return total_distance