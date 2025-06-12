from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        buckets = [[] for _ in range(1, 10)]

        for i in range(1, n + 1):
            temp = i
            while temp > 9:
                temp //= 10

            buckets[temp - 1].append(i)

        for i in range(9):
            buckets[i].sort(key=lambda x: str(x))

        result = []
        for bucket in buckets:
            result.extend(bucket)
        
        return result
