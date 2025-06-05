class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if node1 == target:
                return node2
            
            if node1:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        
        return None