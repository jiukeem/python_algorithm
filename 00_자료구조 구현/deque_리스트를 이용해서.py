# leetcode 641번 문제

# 내풀이 - 리스트(동적배열) 사용
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.l = [None] * k
        self.maxlen = k
        self.start = 0
        self.end = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.l[self.start] = value
        else:
            self.start = (self.start - 1 + self.maxlen) % self.maxlen
            self.l[self.start] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.l[self.end] = value
        else:
            self.end = (self.end + 1) % self.maxlen
            self.l[self.end] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.l[self.start] = None
        self.size -= 1
        if not self.isEmpty():
            self.start = (self.start + 1) % self.maxlen
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.l[self.end] = None
        self.size -= 1
        if not self.isEmpty():
            self.end = (self.end - 1 + self.maxlen) % self.maxlen
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.l[self.start] is None:
            return -1
        return self.l[self.start]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.l[self.end] is None:
            return -1
        return self.l[self.end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.maxlen

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