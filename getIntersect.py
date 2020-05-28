# hashset
class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None



# two pointer
'''
def getIntersect(self, head):
    tortoise = head
    hare = head
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return tortoise
    return None
def detectCycle(self, head):
    if head is None:
        return None
    intersect = self.getIntersect(head)
    if intersect is None:
        return None
    
    ptr1 = head
    ptr2 = intersect

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1
'''