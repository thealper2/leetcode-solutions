from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        queue = []
        n = len(nums)
        root = TreeNode()
        queue.append((root, 0, n - 1))
        
        while queue:
            node, left, right = queue.pop(0)
            mid = left + (right - left) // 2
            node.val = nums[mid]

            if left <= mid - 1:
                node.left = TreeNode()
                queue.append((node.left, left, mid - 1))
            
            if mid + 1 <= right:
                node.right = TreeNode()
                queue.append((node.right, mid + 1, right))
        
        return root