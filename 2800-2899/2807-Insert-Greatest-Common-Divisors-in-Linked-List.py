import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        fast = current_node.next

        while fast:
            new_node = ListNode(
                val=math.gcd(current_node.val, fast.val),
                next=fast
            )            
            current_node.next = new_node
            current_node = fast
            fast = fast.next

        return head