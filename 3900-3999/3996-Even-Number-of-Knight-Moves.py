class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        start = tuple(start)
        target = tuple(target)

        if start == target:
            return True

        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        visited = set()
        queue = [(start, 0)]
        visited.add(start)

        while queue:
            pos, dist = queue.pop(0)

            for dx, dy in moves:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if (nx, ny) == target:
                        return (dist + 1) % 2 == 0

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), dist + 1))

        return False
