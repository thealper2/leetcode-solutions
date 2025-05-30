class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def time_to_minute(date):
            hh, mm = date.split(':')
            return 10 * int(hh[0]) * 60 + 60 * int(hh[1]) + int(mm)

        current_minute = time_to_minute(current)
        correct_minute = time_to_minute(correct)

        count = 0
        while current_minute < correct_minute:
            diff = correct_minute - current_minute
            if diff >= 60:
                current_minute += 60
            elif diff >= 15:
                current_minute += 15
            elif diff >= 5:
                current_minute += 5
            else:
                current_minute += 1

            count += 1

        return count
