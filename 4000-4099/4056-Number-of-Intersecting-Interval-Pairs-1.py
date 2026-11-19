class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                a_start, a_end = intervals[i]
                b_start, b_end = intervals[j]
                if max(a_start, b_start) <= min(a_end, b_end):
                    count += 1

        return count
