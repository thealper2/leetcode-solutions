from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stack = [root]
        left_to_right = True
        result = []

        while stack:
            level_values = []
            next_level = []

            for node in stack:
                level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if not left_to_right:
                level_values.reverse()

            result.append(level_values)
            stack = next_level
            left_to_right = not left_to_right

        return result
