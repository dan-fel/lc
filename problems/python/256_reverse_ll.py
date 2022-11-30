from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.previous = None
        return self.recurse(head)

    def recurse(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return self.previous
        
        current_next = head.next

        if not self.previous:
            head.next = None
        else:
            head.next = self.previous
            
        self.previous = head
        return self.recurse(current_next)

    def print_list(self, head: Optional[ListNode]):
        if not head:
            return
        
        print(head.val)
        self.print_list(head.next)

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Solution()
print(sol.print_list(sol.reverseList(list)))


