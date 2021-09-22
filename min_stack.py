class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack=self.stack+[val]

    def pop(self) -> None:
        self.stack=self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mini=99999999999
        for i in self.stack:
            if mini > i:
                mini=i
        return mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()