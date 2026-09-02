# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        beginning = head
        before = None
        new_head = ListNode(next=head)
        ptr = new_head
        while curr:
            group_k = True
            for _ in range(k):
                if curr:
                    curr = curr.next
                    continue
                group_k = False
            if not group_k:
                break
           
            old_beginning = None
            before = curr
            old_beginning = beginning
            while beginning != curr:
                temp = beginning.next
                beginning.next = before
                before = beginning
                beginning = temp
            ptr.next = before
            ptr = old_beginning
        return new_head.next
        

                
                
                
            # curr now at 4 and end at 3


            
            