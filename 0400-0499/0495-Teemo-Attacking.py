class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration
        for i in range(1, len(timeSeries)):
            last = timeSeries[i] - timeSeries[i - 1]
            if duration < last:
                total += duration
            else:
                total += last

        return total
