from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root):
        if not root:
            return 0
        
        left_height = self.height(root.left)
        if left_height == -1:
            return -1

        right_height = self.height(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0