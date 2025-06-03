from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, root.val, False, False)]
        
        while stack:
            node, current_sum, visited_left, visited_right = stack.pop(0)
            
            if not node.left and not node.right and current_sum == targetSum:
                return True
            
            if node.right and not visited_right:
                stack.append((node, current_sum, visited_left, True))
                stack.append((node.right, current_sum + node.right.val, False, False))
                continue
                
            if node.left and not visited_left:
                stack.append((node, current_sum, True, visited_right))
                stack.append((node.left, current_sum + node.left.val, False, False))
        
        return False