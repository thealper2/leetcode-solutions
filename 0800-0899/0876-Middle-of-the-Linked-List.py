from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		elements = []
		current_node = head

		while current_node:
			elements.append(current_node.val)
			current_node = current_node.next

		n = len(elements) // 2
		current_node = head

		while n:
			current_node = current_node.next
			n -= 1

		return current_node
