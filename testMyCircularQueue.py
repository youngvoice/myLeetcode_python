class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._len = k
        self._buf = [0]*self._len
        self._num = 0
        self._pos = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._buf[(self._pos)] = value
        self._pos = (self._pos + 1)%self._len
        self._num = self._num + 1
        print('after enqueue, the content is ', self._buf, 'pos ', self._pos, 'num ', self._num)
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        #self._pos = (self._pos - 1 + self._len) % self._len
        self._num = self._num - 1
        print('after dequeue, the content is ', self._buf, 'pos ', self._pos, 'num ', self._num)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self._buf[(self._pos - self._num + self._len) % self._len]

        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        

        if self.isEmpty():
            return -1
        return self._buf[(self._pos - 1 + self._len) % self._len]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self._num == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self._num == self._len:
            return True
        else:
            return False
        



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# 确定结点（状态）, 边（转换）
# 队列
# 从队列取一个元素，处理该元素，将相邻结点加入队列