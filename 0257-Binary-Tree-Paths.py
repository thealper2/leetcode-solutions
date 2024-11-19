# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth_first_search(self, node, current_path, result):
        if node == None:
            return
        
        current_path += "->" + str(node.val)

        if node.left == None and node.right == None:
            result.append(current_path)

        if node.left != None:
            self.depth_first_search(node.left, current_path, result)

        if node.right != None:
            self.depth_first_search(node.right, current_path, result)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if root == None:
            return result

        current_path = str(root.val)
        if root.left == None and root.right == None:
            result.append(current_path)

        if root.left != None:
            self.depth_first_search(root.left, current_path, result)

        if root.right != None:
            self.depth_first_search(root.right, current_path, result)

        return result

        