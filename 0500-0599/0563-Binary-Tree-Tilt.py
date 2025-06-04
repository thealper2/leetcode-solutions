from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node):
            if not node:
                return 0
            
            nonlocal total_tilt

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            return node.val + left_sum + right_sum
        
        dfs(root)
        return total_tilt