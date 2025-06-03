from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        total = 0

        while queue:
            node = queue.pop(0)

            if node.left:
                if not node.left.left and not node.left.right:
                    total += node.left.val
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return total