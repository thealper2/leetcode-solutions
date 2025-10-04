from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            level_size = len(stack)
            max_val = float('-inf')
            for _ in range(level_size):
                node = stack.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

            result.append(max_val)

       return result
