from collections import defaultdict
from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(set)
        for user_id, time in logs:
            users[user_id].add(time)

        uams = [0] * k
        for times in users.values():
            uam = len(times)
            if 1 <= uam <= k:
                uams[uam - 1] += 1

        return uams
