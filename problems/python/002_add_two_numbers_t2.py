# Definition for singly-linked list.
from typing import Optional
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        sum = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
                        
            res = v1 + v2 + carry
            carry = res // 10
            res = res % 10
            sum.next = ListNode(res, None)

            sum = sum.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
        
            


        
sol = Solution()

l3 = ListNode(2, ListNode(4, ListNode(3)))
l4 = ListNode(5, ListNode(6, ListNode(4)))

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
sol.print_list(sol.addTwoNumbers(l3, l4))