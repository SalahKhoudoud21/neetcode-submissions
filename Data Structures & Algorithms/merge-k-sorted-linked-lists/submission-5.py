# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode()
        ptr = dummy
        while heap:
            _,i,node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next

    
    #     while len(lists) > 1:
    #         merged_lists = []
    #         for i in range(0, len(lists), 2):
    #             list1 = lists[i]
    #             list2 = lists[i+1] if i+1 < len(lists) else None
    #             merged_lists.append(self.mergedLists(list1, list2))
            
    #         lists = merged_lists
    #     return lists[0]
        
    # def mergedLists(self, list1, list2):
    #     ptr1 = list1
    #     ptr2 = list2
    #     dummy = ListNode()
    #     ptr = dummy
    #     while ptr1 and ptr2:
    #         if ptr1.val < ptr2.val:
    #             ptr.next = ptr1
    #             ptr1 = ptr1.next
    #             ptr = ptr.next
    #         elif ptr1.val > ptr2.val:
    #             ptr.next = ptr2
    #             ptr2 = ptr2.next
    #             ptr = ptr.next
    #         else:
    #             ptr.next = ptr1
    #                 # ptr.next.next = ptr2 wrong cause messes up ptr1
    #             ptr1 = ptr1.next
    #             ptr.next.next = ptr2
    #             ptr2 = ptr2.next
    #             ptr = ptr.next.next   
    #     if ptr1:
    #         ptr.next = ptr1
    #         ptr1 = ptr1.next
    #         ptr = ptr.next
    #     elif ptr2:
    #         ptr.next = ptr2
    #         ptr2 = ptr2.next
    #         ptr = ptr.next
        
    #     return dummy.next


        
        
        
        