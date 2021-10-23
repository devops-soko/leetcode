class MyCircularDeque:

    def __init__(self, k: int):
        self.head = []
        self.tail = []
        self.count = 0
        self.k = k
    def insertFront(self, value: int) -> bool:
        if self.count >= self.k:
            return False
        self.head.append(value)
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count >= self.k:
            return False

        self.tail.append(value)
        self.count += 1
        return True
    
    
    def deleteFront(self) -> bool:
        if self.count ==0:
            return False

        if self.head :
            self.head.pop()
            self.count -=1

        elif self.tail:
            self.tail.pop(0)
            self.count -=1
        return True

    def deleteLast(self) -> bool:
        if self.count ==0:
            return False

        if self.tail:
            self.tail.pop()
            self.count -=1
        elif self.head:
            self.head.pop(0)
            self.count -=1
        return True
    def getFront(self) -> int:
        if self.head:
            return self.head[-1]
        elif self.tail:
            return self.tail[0]
        return -1
        

    def getRear(self) -> int:
        if self.tail:
            return self.tail[-1]
        elif self.head:
            return self.head[0]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()