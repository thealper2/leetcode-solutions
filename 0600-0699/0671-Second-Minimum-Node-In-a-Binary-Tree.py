from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
		queue = [root]

		first_min = float('inf')
		second_min = float('inf')

		while queue:
			n = len(queue)

			node = queue.pop(0)

			if node.val < first_min:
				second_min = first_min
				first_min = node.val

			elif node.val < second_min and node.val != first_min:
				second_min = node.val

			if node.left:
				queue.append(node.left)

			if node.right:
				queue.append(node.right)

		return second_min if second_min != float('inf') else -1
