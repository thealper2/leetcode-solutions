from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if self.isSameTree(node, subRoot):
                return True
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
            
        return True