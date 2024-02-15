from typing import List
import math

#class KthLargest:

    #def __init__(self, k: int, nums: List[int]):

        

    #def add(self, val: int) -> int:
        


class MinHeap:

    def __init__(self, k):
        self.heap = []
        self.capacity = k        

    def bubble_up(self, idx):
        if idx <= 0:
            return                            
        parent = math.ceil(idx / 2) - 1 # 1 / 2 ceil - 1 = 0        
        if self.heap[parent] > self.heap[idx]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]              
            self.bubble_up(parent)

    def bubble_down(self):            
        index = 0
        bubble = self.heap[0]
        

        left = index * 2 + 1
        right = index * 2 + 2
        smallest = self.heap()




        
    def add(self, val):
        if len(self.heap) < self.capacity:            
            self.heap.append(val)
            self.bubble_up(len(self.heap) - 1)

        elif val > self.heap[0]:
            self.heap[0] = val
            self.bubble_down()

min_heap = MinHeap()

min_heap.add(3)
min_heap.add(1)
min_heap.add(6)
min_heap.add(5)
min_heap.add(2)
min_heap.add(4)

print(min_heap.heap)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)