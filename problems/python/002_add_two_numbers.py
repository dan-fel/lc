
from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, list: Optional[ListNode]):
        while list != None:
            print(list.val)
            list = list.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_done = False
        l2_done = False
        add_overflow = 0
        list = ListNode(0, None)
        list_begin = list

        while not (l1_done and l2_done):
            v1 = 0
            v2 = 0
            if not l1_done:
                v1 = l1.val
            
            if not l2_done:
                v2 = l2.val
                
            add_result = v1 + v2 + add_overflow
            if add_result == 10:
                add_result = 0
                add_overflow = 1
                
            elif add_result > 10:
                add_overflow = 1
                add_result = add_result - 10
            else:
                add_overflow = 0

            list.val = add_result

            if l1.next != None and l2.next != None:
                l1 = l1.next
                l2 = l2.next
                list.next = ListNode(0, None)
                list = list.next

            elif l1.next == None and l2.next == None:
                l1_done = True
                l2_done = True
                if add_overflow > 0:
                    list.next = ListNode(1, None)

            elif l1.next == None and l2.next != None:
                l2 = l2.next
                l1_done = True
                list.next = ListNode(0, None)
                list = list.next

            elif l1.next != None and l2.next == None:
                l1 = l1.next
                l2_done = True
                list.next = ListNode(0, None)
                list = list.next
        return list_begin        

sol = Solution()

list1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
list2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

sol.printList(sol.addTwoNumbers(list1, list2))