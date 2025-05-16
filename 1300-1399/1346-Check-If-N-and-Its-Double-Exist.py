from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True


        return False