from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [source]
        visited[source] = True
        
        while queue:
            edge = queue.pop(0)

            if edge == destination:
                return True

            for neighbor in graph[edge]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
