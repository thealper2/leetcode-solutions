from typing import List


class Solution:
    def sampleStats(self, arr: List[int]) -> List[float]:
        total = sum(arr)
        
        # Min
        minimum = next(i for i in range(256) if arr[i] > 0)
        
        # Max
        maximum = next(i for i in range(255, -1, -1) if arr[i] > 0)
        
        # Mean
        total_sum = sum(i * arr[i] for i in range(256))
        mean = total_sum / total

        # Median
        if total % 2 == 1:
            target = total // 2
            cum = 0
            for i in range(256):
                cum += arr[i]
                if cum > target:
                    median = i
                    break

        else:
            target1 = total // 2 - 1
            target2 = total // 2
            cum = 0
            first_val  = -1
            for i in range(256):
                cum += arr[i]
                if first_val == -1 and cum > target1:
                    first_val = i

                if cum > target2:
                    median = (first_val + i) / 2.0
                    break

        # Mode
        mode = max(range(256), key=lambda i: arr[i])
        return [float(minimum), float(maximum), mean, median, float(mode)]
