from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 0:
            return []

        if n == 1:
            return ['0', '1']

        prev = ['0', '1']
        for _ in range(2, n + 1):
            current = []
            for s in prev:
                if s[-1] == '1':
                    current.append(s + '0')
                
                current.append(s + '1')

            prev = current

        return prev
