class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            min_val = min(val, self.minStack[-1])
            self.minStack.append(min_val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-1)
minStack.push(0)
minStack.push(-3)
minStack.push(-21)

print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
print(minStack.top())
