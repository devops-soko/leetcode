class MyCircularDeque:
    
    def __init__(self, k: int):
        self.head = []
        self.tail = []
        self.k = k
        self.count = 0 

    def insertFront(self, value: int) -> bool:
        if self.k <= self.count :
            return False

        self.head.append(value)
        self.count +=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k <= self.count :
            return False

        self.tail.append(value)
        self.count +=1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0 :
            return False
        
        if self.head:
            self.head.pop()
            
        elif self.tail:
            self.tail.pop(0)

        self.count -=1
        return True
    def deleteLast(self) -> bool:
        if self.count == 0 :
            return False
        
        if self.tail:
            self.tail.pop()
            
        elif self.head:
            self.head.pop(0)

        self.count -=1
        return True

    def getFront(self) -> int:
        if self.head :
            return self.head[-1]
        elif self.tail :
            return self.tail[0]
        else :
            return -1

    def getRear(self) -> int:
        if self.tail :
            return self.tail[-1]
        elif self.head :
            return self.head[0]
        else :
            return -1

    def isEmpty(self) -> bool:
        return self.count ==0

    def isFull(self) -> bool:
        return self.count == self.k