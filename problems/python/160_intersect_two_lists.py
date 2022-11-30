from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2:             
            #l1 = l1.next if l1 else headB
            #l2 = l2.next if l2 else headA
        return l1


l1 = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
l2 = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))

sol = Solution()
print(sol.getIntersectionNode(l1, l2))

 