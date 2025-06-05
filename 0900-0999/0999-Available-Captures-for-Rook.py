from typing import List


class Solution:
	def numRookCaptures(self, board: List[List[str]]) -> int:
		for i in range(8):
			for j in range(8):
				if board[i][j] == 'R':
					x, y = i, j
					break

			else:
				continue

			break

		count = 0
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			while 0 <= nx < 8 and 0 <= ny < 8:
				if board[nx][ny] == 'p':
					count += 1
					break

				if board[nx][ny] == 'B':
					break

				nx += dx
				ny += dy

		return count
