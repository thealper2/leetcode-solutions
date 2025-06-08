from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_people = defaultdict(list)
        result = []
        
        for person, size in enumerate(groupSizes):
            size_to_people[size].append(person)
        
        for size, people in size_to_people.items():
            for i in range(0, len(people), size):
                result.append(people[i:i + size])
        
        return result