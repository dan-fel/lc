from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2
                
        return head.next

    def print_list(self, list: Optional[ListNode]):
        while list:
            print(list.val)
            list = list.next

                
sol = Solution()

sol.print_list(sol.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))
sol.print_list(sol.mergeTwoLists(ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6)))))
sol.print_list(sol.mergeTwoLists(None, None))
sol.print_list(sol.mergeTwoLists(None, ListNode(0)))

            

    
                




