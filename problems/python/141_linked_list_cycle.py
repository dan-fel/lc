from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False
        fast, slow = head.next, head

        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next
        
        return False


            
        

begin = ListNode(0)
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, begin))))
l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
begin.next = list

sol = Solution()
print(sol.hasCycle(begin))
print(sol.hasCycle(l2))

