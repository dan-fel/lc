class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev   

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.head = None
        self.end = None
        self.capacity = capacity
        self.cache_size = 0
        
    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        node = self.keys[key]

        # if the next node is None, that means we have an end node and the self.end shall be replaced.
        if not node.next:
            self.end = node.prev

        if node.prev:

            # prev shall point to next node.
            node.prev.next = node.next

            # insert node at front now.
            temp = self.head
            temp.prev = node
            self.head = node
            self.head.next = temp
            self.head.prev = None

        return node.val

    def put(self, key: int, value: int) -> None:            
        if not self.head:
            self.head = Node(key, value)
            self.end = self.head                        
            self.keys[key] = self.head
            self.cache_size += 1
        else:            
            # Add new cache item in front
            temp = self.head
            self.head = Node(key, value, next = temp)
            temp.prev = self.head
            self.keys[key] = self.head
            self.cache_size += 1
            
            # Remove item at the end.
            if self.cache_size > self.capacity:
                temp = self.end
                self.end = self.end.prev
                self.end.next = None                
                self.keys.pop(temp.key)
                self.cache_size -= 1
                
    def print_keys(self):
        print(self.keys)

    def print_list(self):
        head = self.head
        while head:
            print(head.val)
            head = head.next

sol = LRUCache(1)
sol.put(2,1)
sol.print_list()
sol.get(2)
sol.put(3,2)
# sol.get(2)
# sol.get(3)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)