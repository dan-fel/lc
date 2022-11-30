from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) and O(n) solution.
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        front = 0
        back = len(values) - 1
        
        grab_from_front = True

        while front != back:
            
            if grab_from_front:
                head.val = values[front]
                front += 1
                grab_from_front = False
                
            else:
                head.val = values[back]
                back -= 1
                grab_from_front = True        
            
            head = head.next
        head.val = values[front]
    # O(n) and space O(1)
    def reorderListConstantMem(self, head: Optional[ListNode]) -> None:
        # Get length
        current = head
        
        length = 0
        while current:
            length += 1
            current = current.next

        # Get the count where we should split the list.
        count = 0
        prev = None
        current = head
        while count < int(length / 2):
            prev = current
            current = current.next 
            count += 1 
            

        tempish = prev.next
        prev.next = None
        # Reverse the back end of the list!
        prev = None            

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = temp
        back = prev
        get_from_back = True
        current = head
        while current and back:            
            if get_from_back:                
                # Store temporary variables for next nodes for front and back ptr.
                tmp_back = back.next
                tmp = current.next
                
                # Swap current next to back.
                current.next = back
                back.next = tmp                
                
                # Move our back and front pointers
                back = tmp_back
                current = current.next

                get_from_back = False
            
            else:                
                prev = current
                current = current.next
                get_from_back = True
        if back:
            prev.next = back        

        return head     
    # O(n) and space O(1)
    def reorderListConstantMemFast(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:            
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the back end of the list!
        
        back = slow.next
        prev = slow.next = None

        while back:
            # Store pointer to the next element in the list
            tmp = back.next
            # Set the current pointer to the previous element
            back.next = prev
            # Update our previous element with current
            prev = back
            # Update current so that it moves forward in the list.
            back = tmp
        
        front, back = head, prev        
        # Since len(back) < len(front), always.
        while back:                 
            tmp1 = back.next
            tmp2 = front.next

            front.next = back
            back.next = tmp2

            back = tmp1        
            front = tmp2            
        # a --> b --> .. to a --> x --> b <-- and we are at b now
        # after inserting the element

        self.print_list(head)   
        
    def print_list(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next
        
            

# Expected result: 5 5 6 4 1 8
l2 = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))

l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

l4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Solution()

#sol.print_list(sol.reorderListConstantMem(l3))
#sol.print_list(sol.reorderListConstantMem(l3))
#sol.print_list(sol.reorderListConstantMem(l4))
sol.print_list(sol.reorderListConstantMemFast(l3))
# sol.print_list(l2)
# sol.reorderList(l2)
# print("AFTER")
# sol.print_list(l2)
        