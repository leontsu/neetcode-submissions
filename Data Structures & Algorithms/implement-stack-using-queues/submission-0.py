class MyStack:

    def __init__(self):
        self.mainQueue = deque()
        self.tempQueue = deque()

    def push(self, x: int) -> None:
        self.tempQueue.append(x)
        while self.mainQueue:
            self.tempQueue.append(self.mainQueue.popleft())
        self.mainQueue, self.tempQueue = self.tempQueue, self.mainQueue

    def pop(self) -> int:
        return self.mainQueue.popleft()

    def top(self) -> int:
        return self.mainQueue[0]

    def empty(self) -> bool:
        return True if not self.mainQueue else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()