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
        

        copy = head.next
        curr = head
        # now separating copied nodes and original nodes
        while curr:
            copy_ptr = curr.next
            curr.next = copy_ptr.next
            if copy_ptr.next:
                copy_ptr.next = copy_ptr.next.next
            curr = curr.next
        
        return copy


