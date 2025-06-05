from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
		x_info = {'depth': 0, 'parent': None}
		y_info = {'depth': 0, 'parent': None}

		queue = [(root, 0, None)] # (node, depth, parent)

		while queue:
			node, depth, parent = queue.pop(0)

			if node.val == x:
				x_info['depth'] = depth
				x_info['parent'] = parent

			elif node.val == y:
				y_info['depth'] = depth
				y_info['parent'] = parent

			if node.left:
				queue.append((node.left, depth + 1, node))

			if node.right:
				queue.append((node.right, depth + 1, node))

		return x_info['depth'] == y_info['depth'] and x_info['parent'] != y_info['parent']
