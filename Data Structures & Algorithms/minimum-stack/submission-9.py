class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if self.minVal is None: 
            self.minVal = val

        self.stack.append(val)
        self.minVal = min(val, self.minVal) 

    def pop(self) -> None:
        if not self.stack: return 

        self.stack.pop()
        self.minVal = self.findNewMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal

    def findNewMin(self) -> int:
        if self.stack: 
            return min(self.stack)
        
