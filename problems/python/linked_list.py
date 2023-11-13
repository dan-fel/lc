from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):        
        self.head = None
        self.end = None
    
    def get(self, index: int) -> int:
        current_node = self.head
        for i in range(0, index):
            if index == i:
                return current_node.value
            else:
                current_node = current_node.next
                
        return -1    
        
    def insertHead(self, val: int) -> None:
        if not self.head: 
            self.head = Node(val)
            self.head.next = self.end            
        else:
            new_head = Node(val, self.head)
            self.head = new_head
        
    def insertTail(self, val: int) -> None:
        if not self.end:
            self.end = Node(val)
            self.head.next = self.end
        else:
            new_end = Node(val)
            self.end.next = new_end
            self.end = new_end

    
        
    def remove(self, index: int) -> bool:        
        return False

    def getValues(self) -> List[int]:
        return []

ll = LinkedList()


ll.insertHead()
