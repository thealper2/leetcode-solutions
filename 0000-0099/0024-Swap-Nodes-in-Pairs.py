from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_node, current_node = dummy, head

        while current_node and current_node.next:
            first = current_node
            second = current_node.next

            prev_node.next = second
            first.next = second.next
            second.next = first

            prev_node = first
            current_node = first.next

        return dummy.next
