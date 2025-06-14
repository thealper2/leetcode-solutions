from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [True] + [False] * (n - 1)
        stack = [0]

        while stack:
            room = stack.pop(0)
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)