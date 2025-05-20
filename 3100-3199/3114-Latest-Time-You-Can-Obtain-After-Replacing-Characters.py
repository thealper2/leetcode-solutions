class Solution:
    def findLatestTime(self, s: str) -> str:
        hour, minute = s.split(":")

        if hour == '??':
            hour = '11'

        if minute == '??':
            minute = '59'

        if hour[0] == '?':
            if hour[1] == '1' or hour[1] == '0':
                hour = '1' + hour[1]

            else:
                hour = '0' + hour[1]

        if hour[1] == '?':
            hour = hour[0] + ('9' if hour[0] == '0' else '1')

        if minute[0] == '?':
            minute = '5' + minute[1]

        if minute[1] == '?':
            minute = minute[0] + '9'

        return f"{hour}:{minute}"
