from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n

        def is_safe(node):
            if state[node] > 0:
                return state[node] == 2

            state[node] = 1
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False

            state[node] = 2
            return True

        safe_nodes = []
        for i in range(n):
            if is_safe(i):
                safe_nodes.append(i)

        return safe_nodes
