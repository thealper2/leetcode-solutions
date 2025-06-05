from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        idx = 0
        n = len(arr)
    
        while idx <= n - 1:
            pattern = arr[idx:idx+m]
            if pattern * k == arr[idx:idx+m*k]:
                return True

            idx += 1

        return False
