class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) > 0 and val > self.mins[-1]:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        
        return self.mins[-1]
        
