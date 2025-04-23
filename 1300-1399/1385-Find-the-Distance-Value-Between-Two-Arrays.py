from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        for num in arr1:
            left, right = 0, len(arr2) - 1
            pos = len(arr2)

            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] >= num:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1

            valid = True
            if pos < len(arr2) and abs(arr2[pos] - num) <= d:
                valid = False

            if pos > 0 and abs(arr2[pos - 1] - num) <= d:
                valid = False

            if valid:
                distance_value += 1

        return distance_value