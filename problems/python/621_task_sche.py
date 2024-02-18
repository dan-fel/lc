# Idea.. 

# Use a min heap to 

from typing import List
import heapq
from collections import Counter
import queue


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, prio):
        heapq.heappush(self.queue, (prio, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]
    
    def __len__(self):
        return len(self.queue)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        tasks_map, heap = Counter(tasks), []        
        for t in tasks_map:            
            heapq.heappush(heap, (-tasks_map[t], t))

        pqueue = PriorityQueue()

        step = 0
        while heap or pqueue:
            if heap:
                task = heapq.heappop(heap)
                task = (task[0] + 1, task[1])
            
                if task[0] != 0:            
                    pqueue.push(task, step + n)

            if pqueue and pqueue.queue[0][0] == step:                     
                task = pqueue.pop()
                heapq.heappush(heap, task)       
                    
            step += 1
        
        return step

sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))