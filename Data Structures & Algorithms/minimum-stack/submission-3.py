class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        
        min_heap = self.stack.copy()
        heapq.heapify(min_heap)
        return heapq.heappop(min_heap)
        
