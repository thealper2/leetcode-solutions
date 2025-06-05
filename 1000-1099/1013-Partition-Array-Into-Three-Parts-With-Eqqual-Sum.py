from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        current = 0
        count = 0
        n = len(arr)

        for i in range(n):
            current += arr[i]
            if current == target:
                count += 1
                current = 0
                if count == 2 and i < n -1:
                    return sum(arr[i+1:]) == target

        return False
