from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        fast = head.next
        
        while fast:
            new_val = 0
            while fast and fast.val != 0:
                new_val += fast.val
                fast = fast.next
            
            current_node.val = new_val
            
            if fast and fast.next:
                current_node.next = fast
                current_node = fast
                fast = fast.next
            else:
                current_node.next = None
                break
        
        return head