class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.swap = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.swap.append(self.stack.pop())
        self.stack.append(x)
        while self.swap:
            self.stack.append(self.swap.pop())

        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()