from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        stack = [(root, None, None)]

        while stack:
            node, parent, grandparent = stack.pop()
            if grandparent and grandparent.val % 2 == 0:
                total += node.val

            if node.left:
                stack.append((node.left, node, parent))
            
            if node.right:
                stack.append((node.right, node, parent))

        return total
