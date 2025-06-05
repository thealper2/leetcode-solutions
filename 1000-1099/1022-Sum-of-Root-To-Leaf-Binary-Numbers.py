from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum_ = 0
        queue = [(root, str(root.val))]

        while queue:
            node, val = queue.pop(0)

            if not node.left and not node.right:
                sum_ += int(val, 2)

            if node.left:
                queue.append((node.left, val + str(node.left.val)))

            if node.right:
                queue.append((node.right, val + str(node.right.val)))

        return sum_