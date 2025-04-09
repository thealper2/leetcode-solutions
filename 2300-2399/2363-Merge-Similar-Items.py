from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for value, weight in items1:
            if value in d:
                d[value] += weight
            else:
                d[value] = weight

        for value, weight in items2:
            if value in d:
                d[value] += weight
            else:
                d[value] = weight

        values = list(d.keys())
        n = len(values)

        for i in range(n):
            for j in range(0, n-i-1):
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]
        
        result = [[value, d[value]] for value in values]
        return result