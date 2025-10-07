from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = [i for i in range(numCourses) if indegree[i] == 0]
        visited = 0
        while q:
            course = q.pop(0)
            visited += 1
            for n in graph[course]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return visited == numCourses
