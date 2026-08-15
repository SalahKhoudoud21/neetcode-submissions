class Node:  # doubly linked list
    def __init__(self, key: int, value: int, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = Node(0, 0)
        self.ptr = self.cache
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        reference = self.hash_map[key]  # location
        if reference != self.ptr:
            reference.prev.next = reference.next
            if reference.next:
                reference.next.prev = reference.prev
            reference.prev = self.ptr
            reference.next = None
            self.ptr.next = reference
            self.ptr = self.ptr.next
        return reference.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            reference = self.hash_map[key]
            reference.value = value # udpate the value
            if reference != self.ptr:
                reference.prev.next = reference.next
                if reference.next:
                    reference.next.prev = reference.prev
                
                reference.prev = self.ptr
                reference.next = None
                self.ptr.next = reference
                self.ptr = self.ptr.next
        
        else:
            if len(self.hash_map) == self.size:
                lru = self.cache.next
                del self.hash_map[lru.key]
                self.cache.next = lru.next
                if self.cache.next:
                    self.cache.next.prev = self.cache
                else:
                    self.ptr = self.cache
            new_reference = Node(key, value, prev=self.ptr)
            self.ptr.next = new_reference
            self.ptr = self.ptr.next
            self.hash_map[key] = new_reference
                
