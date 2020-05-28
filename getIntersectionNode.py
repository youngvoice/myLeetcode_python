# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        if not pa or not pb:
            return None
        while pa and pb:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next

        if not pa and not pb:
            return None
        
        if not pa:
            pa = headB
        else:
            pb = headA

        while pa and pb:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        if not pa:
            pa = headB
        else:
            pb = headA
        
        while pa and pb:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
    
        return None

