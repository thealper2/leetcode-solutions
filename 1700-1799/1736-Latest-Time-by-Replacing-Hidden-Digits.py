class Solution:
    def maximumTime(self, time: str) -> str:
        hh, mm = list(time[:2]), list(time[3:])
        
        if hh[0] == '?' and hh[1] == '?':
            hh = ['2', '3']
        else:
            if hh[0] == '?':
                hh[0] = '2' if (hh[1] == '?' or int(hh[1]) <= 3) else '1'
            if hh[1] == '?':
                hh[1] = '3' if hh[0] == '2' else '9'
        
        if mm[0] == '?' and mm[1] == '?':
            mm = ['5', '9']
        else:
            if mm[0] == '?':
                mm[0] = '5'
            if mm[1] == '?':
                mm[1] = '9'
        
        return f"{''.join(hh)}:{''.join(mm)}"
