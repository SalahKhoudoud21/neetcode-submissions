# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_l1 = l1
        ptr_l2 = l2
        summa_list = ListNode()
        curr_ptr = summa_list
        carry = 0
        while l1 or l2:
            if l1 and l2:
                summa = l1.val + l2.val + carry
                carry = summa // 10 # 18 => 1
                l1, l2 = l1.next, l2.next
            elif l1:
                summa = l1.val + carry
                l1 = l1.next
            else:
                summa = l2.val + carry
                l2 = l2.next
            carry = summa // 10
            curr_ptr.next = ListNode(summa % 10)
            curr_ptr = curr_ptr.next
        if carry != 0:
            curr_ptr.next = ListNode(carry)
        return summa_list.next
            
