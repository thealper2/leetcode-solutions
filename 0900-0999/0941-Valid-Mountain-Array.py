from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        left, right = 0, n - 1
        
        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1
        
        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1
        
        return left == right and left != 0 and right != n - 1