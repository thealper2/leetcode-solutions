from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [(root, 0, None)]
        parent = {}
        max_depth = 0
        deepest = []
        
        while stack:
            node, depth, par = stack.pop()
            parent[node] = par
            
            if depth > max_depth:
                max_depth = depth
                deepest = [node]
            elif depth == max_depth:
                deepest.append(node)
            
            if node.right:
                stack.append((node.right, depth + 1, node))
            if node.left:
                stack.append((node.left, depth + 1, node))
        
        while len(deepest) > 1:
            ancestors = set()
            for i, node in enumerate(deepest):
                deepest[i] = parent[node]
                ancestors.add(parent[node])
            if len(ancestors) == 1:
                return deepest[0]
        
        return deepest[0]
