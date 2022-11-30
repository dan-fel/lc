from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while head:    
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev 

    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        list = []
        while head:
            list.append(head.val)
            head = head.next

        for i in range(0, int(len(list)/2)):
            if list[i] != list.pop():
                return False

        return True

    def print_list(self, list: ListNode):        
        while list:
            print(list.val)
            list = list.next
            
            

sol = Solution()

#sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))))

