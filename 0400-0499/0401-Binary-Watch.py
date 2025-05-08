from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []

        for h in range(12):
            for m in range(60):
                ht = h
                ht_count = 0
                while ht >= 1:
                    ht_count += (ht % 2)
                    ht //= 2
                
                mt = m
                mt_count = 0
                while mt >= 1:
                    mt_count += (mt % 2)
                    mt //= 2

                if mt_count + ht_count == turnedOn:
                    times.append(f'{h}:{m:02d}')

                
        return times