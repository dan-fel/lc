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
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:    
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
                                        
        while prev:         
            print(head.val, prev.val)   
            if head.val != prev.val:
                return False
            
            prev = prev.next
            head = head.next

        return True
        

    def print_list(self, list: ListNode):        
        while list:
            print(list.val)
            list = list.next
            
            

sol = Solution()

print(sol.isPalindrome(ListNode(1, ListNode(2))))
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))))

# def reverse(self, head: Optional[ListNode]) -> ListNode:
#         prev = None
#         while head:    
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
        
#         return prev
        
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         p1_head = head
#         p2_head = head

#         p1_count = 1
#         p2_count = 1

#         while p2_head.next:
#             if p2_head.next.next:                          
#                 p2_head = p2_head.next.next
#                 p2_count += 2
#             else:
#                 break

#             if p1_head.next:                
#                 p1_head = p1_head.next
#                 p1_count += 1
                        
#         if (2 * p1_count - 1) == p2_count:            
#             reversed_list = self.reverse(p1_head.next)                        
#             while reversed_list:                
#                 if head.val != reversed_list.val:
#                     return False
                
#                 head = head.next
#                 reversed_list = reversed_list.next

#             return True