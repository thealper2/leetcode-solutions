from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
		prev = None
		is_univalued = True

		def inorder(node):
			if not node:
				return

			nonlocal prev, is_univalued
			current_val = node.val

			if not prev:
				prev = current_val
			else:
				if prev != current_val:
					is_univalued = False

			inorder(node.left)
			inorder(node.right)

		inorder(root)
		return is_univalued
