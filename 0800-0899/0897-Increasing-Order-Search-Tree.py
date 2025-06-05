from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		elements = []

		def inorder(node):
			if not node:
				return

			inorder(node.left)
			elements.append(node.val)
			inorder(node.right)

		inorder(root)

		n = len(elements)
		dummy = TreeNode()
		order_tree = dummy

		for i in range(n):
			dummy.right = TreeNode(elements[i])
			dummy = dummy.right

		return order_tree.right
