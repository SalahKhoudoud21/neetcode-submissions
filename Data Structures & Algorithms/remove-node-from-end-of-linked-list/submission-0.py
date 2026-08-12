# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right_ptr = head
        count = 0
        while count < n:
            right_ptr = right_ptr.next
            count += 1
        dummy_node = ListNode(next=head)
        left_ptr = dummy_node
        while right_ptr:
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next
        left_ptr.next = left_ptr.next.next
        return dummy_node.next
            