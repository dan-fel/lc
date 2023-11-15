from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next
    
class LinkedList:
    def __init__(self):        
        self.head = None
        self.end = None
    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current:        
            if index == i:
                return current.value
            else:
                current = current.next
            i += 1

        return -1    
         
    def insertHead(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
            self.end = self.head
        else:
            new_head = Node(val, self.head)
            self.head = new_head
 
        
    def insertTail(self, val: int) -> None:
        if not self.end:
            self.end = Node(val)
            self.head = self.end
        else:
            new_end = Node(val)
            self.end.next = new_end
            self.end = self.end.next

    
    def remove(self, index: int) -> bool:        
        if not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        prev = None
        current = self.head
        i = 0

        while current:            
            if index == i:
                if current == self.end:
                    self.end = prev
                    self.end.next = None
                else:
                    prev.next = current.next                
                return True                
            else:                    
                prev = current
                current = current.next

            i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values
    
    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

ll = LinkedList()

ll.insertTail(1)
ll.insertTail(2)
print(ll.get(1))
print(ll.remove(1))

ll.insertTail(2)
print(ll.getValues())
print(ll.get(1))
print(ll.get(0))

print(ll.getValues())





