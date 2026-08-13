"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        # adding copy nodes in the head list
        while curr:
            temp = curr.next
            new_node = Node(curr.val, temp)
            curr.next = new_node
            curr = temp
        
        ptr = head
        # now refering randoms to the copied randoms for the copied nodes
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        

        og_ptr = head
        copy = head.next
        copy_ptr = head.next
        # now separating copied nodes and original nodes
        while og_ptr:
            og_ptr.next = copy_ptr.next
            og_ptr = og_ptr.next
            if og_ptr:
                copy_ptr.next = og_ptr.next
                copy_ptr = copy_ptr.next
        
        return copy


