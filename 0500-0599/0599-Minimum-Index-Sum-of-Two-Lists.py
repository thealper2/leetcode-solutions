from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n, m = len(list1), len(list2)
        both = []
        result = []
        minimum_index = float('inf')
        for i in range(n):
            for j in range(m):
                if list1[i] == list2[j]:
                    both.append((list1[i], i + j))
                    if i + j < minimum_index:
                        minimum_index = i + j

        for x in both:
            if x[1] == minimum_index:
                result.append(x[0])

        return result