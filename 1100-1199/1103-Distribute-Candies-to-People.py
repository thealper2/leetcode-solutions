from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0 for _ in range(num_people)]
        candy = 1

        while candies:
            for i in range(num_people):
                if candy + 1 <= candies:
                    people[i] += candy
                    candies -= candy
                    candy += 1
                else:
                    people[i] += candies
                    candies -= candies

        return people