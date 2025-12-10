from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        stack = [(0, [0])]

        while stack:
            node, path = stack.pop()
            if node == n - 1:
                paths.append(path)
                continue

            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))

        return paths
