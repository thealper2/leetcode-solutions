from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
		elements1 = []
		elements2 = []

		def preorder(node, elements):
			if not node:
				return

			if not node.left and not node.right:
				elements.append(node.val)

			preorder(node.left, elements)
			preorder(node.right, elements)

		preorder(root1, elements1)
		preorder(root2, elements2)

		return elements1 == elements2
