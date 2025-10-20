from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        stack = [root]
        leftmost = root.val

        while stack:
            level_size = len(stack)
            leftmost = stack[0].val
            for _ in range(level_size):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

        return leftmost
