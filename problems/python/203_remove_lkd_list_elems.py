from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            if current.val == val:
                if prev == None:                    
                    head = current.next
                    current = current.next
                else:                                        
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next
        return head
    
    def print_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            print(head.val)
            head = head.next

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
l2 = ListNode(1, ListNode(2))
sol = Solution()
sol.print_list(l1)
sol.removeElements(l1, 2)

print("-----")
sol.print_list(l1)
print("-----")
sol.removeElements(l2, 2)