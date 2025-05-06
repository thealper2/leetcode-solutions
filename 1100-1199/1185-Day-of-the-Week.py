class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        # Zeller's Congruence
        day_of_week = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[day_of_week]