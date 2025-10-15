from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy

        while current_node.next:
            if current_node.next.val in nums:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
            
        return dummy.next
