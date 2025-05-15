class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def dayOfYear(date: str) -> int:
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

            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                months["2"] = 29

            total_days = 0
            for m in range(1, month):
                total_days += months[str(m)]

            for y in range(1971, year):
                if (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0):
                    total_days += 1

            return 365 * year + total_days + day

        d1 = dayOfYear(date1)
        d2 = dayOfYear(date2)
        return abs(d1 - d2)