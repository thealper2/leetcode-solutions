# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def total_complete_nodes(self, node):
        if node == None:
            return 0

        l = self.total_complete_nodes(node.left)
        r = self.total_complete_nodes(node.right)
        return 1 + l + r

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        result = self.total_complete_nodes(root)
        return result

        