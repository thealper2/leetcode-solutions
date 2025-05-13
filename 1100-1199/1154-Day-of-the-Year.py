class Solution:
    def dayOfYear(self, date: str) -> int:
        months = {
            "1": 31, "2": 28, "3": 31,
            "4": 30, "5": 31, "6": 30,
            "7": 31, "8": 31, "9": 30,
            "10": 31, "11": 30, "12": 31
        }

        year, month, day = date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)

        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            months["2"] = 29

        total_days = 0
        for m in range(1, month):
            total_days += months[str(m)]

        return total_days + day