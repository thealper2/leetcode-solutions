class Solution:
    def countTime(self, time: str) -> int:
        hour, minute = time.split(':')

        possible_hours = 1
        
        if (hour == '??'):
            possible_hours *= 24
        elif (hour[0] == '?' and int(hour[1]) >= 4):
            possible_hours *= 2
        elif (hour[0] == '?' and int(hour[1]) <= 4):
            possible_hours *= 3
        elif (int(hour[0]) <= 1 and hour[1] == '?'):
            possible_hours *= 10
        elif (int(hour[0]) == 2 and hour[1] == '?'):
            possible_hours *= 4
        
        if (minute == '??'):
            possible_hours *= 60
        elif (minute[0] == '?'):
            possible_hours *= 6
        elif (minute[1] == '?'):
            possible_hours *= 10

        return possible_hours