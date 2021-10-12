class MyQueue:
    
    def __init__(self):
        self.s = collections.deque()

    def push(self, x: int) -> None:
        d = collections.deque()
        for _ in range(len(self.s)) :
            d.append(self.s.pop()) 

        self.s.append(x)
        for _ in range(len(d)):
            self.s.append(d.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()