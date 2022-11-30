from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.H = []
        for n in nums:
            self.add_init(n)

    def swap(self, val_index: int, p_index: int):        
        temp = self.H[p_index]
        self.H[p_index] = self.H[val_index]
        self.H[val_index] = temp

    def bubble_up(self, val):
        val_index = len(self.H) - 1
        bubble = True
        while bubble:
            parent_index = max(0, int((val_index + 1) / 2) - 1)
            if self.H[val_index] < self.H[parent_index]:
                self.swap(val_index, parent_index)
                val_index = parent_index
            else:
                bubble = False

    def smallerChild(self, left, right) -> int:
        heap_size = len(self.H)
        if left < heap_size and right < heap_size:
            if self.H[left] < self.H[right]:
                return left
            elif self.H[left] > self.H[right]:
                return right
            else:
                return left
        elif left < heap_size and right >= heap_size:            
            return left
        elif left >= heap_size and right < heap_size:
            return right
        else:
            return -1

    def bubble_down(self, val):        
        self.H[0] = val
        val_index = 0
        heap_size = len(self.H)
        bubble = True

        while bubble:
            left_index = 2 * val_index + 1
            right_index = 2 * val_index + 2
            smallest_val_index = self.smallerChild(left_index, right_index)
            if smallest_val_index == -1:
                bubble = False
            elif self.H[smallest_val_index] < val:
                print("swapping")
                self.swap(val_index, smallest_val_index)
                val_index = smallest_val_index
            else:
                bubble = False

    def add_init(self, val: int) -> int:        
        if not self.H:            
            self.H.append(val)
            print(self.H)

        elif len(self.H) <= self.k:
            print("not full list")
            self.H.append(val)
            self.bubble_up(val)
        else: 
            if val > self.H[0]:                
                self.bubble_down(val)

    def add(self, val: int) -> int:
        print(val)
        self.add_init(val)                        
        if len(self.H) > self.k:
            self.H[0] = self.H[-1]        
            self.bubble_down(self.H[0])
            self.H.pop()        
        else:
            self.bubble_down(self.H[0])
        return self.H[0]             

# obj = KthLargest(1, [])
# print(obj.H)       
# print(obj.add(-3))
# print(obj.H)       
# print(obj.add(-4))
# print(obj.add(0))
# print(obj.add(4))
# print(obj.H)       

# obj = KthLargest(3, [4, 5, 8, 2])
# print(obj.add(3))
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))
# print(obj.H)