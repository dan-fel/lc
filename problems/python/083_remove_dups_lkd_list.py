from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, current = head, head.next        
        while current:
            if prev.val == current.val:
                if not current.next:
                    prev.next = None
                    break                    
                else:
                    current = current.next
            else:
                prev.next = current
                prev = current                
                current = current.next
        return head

    def print_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            print(head.val)
            head = head.next

l1 = ListNode(2, ListNode(2, ListNode(2, ListNode(4, ListNode(8, ListNode(12))))))
l2 = ListNode(1, ListNode(2))
sol = Solution()
sol.deleteDuplicates(l1)
sol.print_list(l1)

# print("-----")
# sol.print_list(l1)
# print("-----")
# sol.deleteDuplicates(l2, 2)