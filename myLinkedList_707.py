# have many program problem
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = ListNode(val)
        new.next = self.head.next
        self.head = new.next

        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = ListNode(val)
        cur = self.head
        if cur.next != None:
            cur = cur.next
        cur.next = new
        self.length += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return None
        if index < 0:
            index = 0
        cur = self.head
        new = ListNode(val)
        for _ in range(index):
            cur = cur.next
        cur.next = new

        self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.length: 
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

'''
# to debug the above program
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        
        print("enter get")
        cur = self.head
        while cur:
            print("element: ", cur.val)
            cur = cur.next
        cur = self.head
        while cur:
            print("get: ", cur.val)
            cur = cur.next
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        print("enter addAtHead")
        cur = self.head
        while cur:
            print("element: ", cur.val)
            cur = cur.next
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new

        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        print("enter addAtTail")
        cur = self.head
        while cur:
            print("element: ", cur.val)
            cur = cur.next
        new = ListNode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new
        self.length += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return None
        if index < 0:
            index = 0

        print("enter addAtIndex")
        cur = self.head
        while cur:
            print("element: ", cur.val)
            cur = cur.next
        cur = self.head
        new = ListNode(val)
        for _ in range(index):
            cur = cur.next
        new.next = cur.next
        cur.next = new

        self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.length: 
            print("enter deleteAtIndex")
            cur = self.head
            while cur:
                print("element: ", cur.val)
                cur = cur.next
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
'''

# remove the debug part
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        
        cur = self.head
        while cur:
            cur = cur.next
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new

        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        new = ListNode(val)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new
        self.length += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return None
        if index < 0:
            index = 0

        cur = self.head
        new = ListNode(val)
        for _ in range(index):
            cur = cur.next
        new.next = cur.next
        cur.next = new

        self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index and index < self.length: 
            
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)