from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(num):
            count = 0
            while num > 0:
                count += num % 2
                num = num // 2

            return count

        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                ones_j = count_bits(arr[j])
                ones_j1 = count_bits(arr[j + 1])

                if ones_j > ones_j1:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                elif ones_j == ones_j1:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr