# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = "", ""
        while(l1.next):
            s1 += str(l1.val)
            l1 = l1.next
        s1 += str(l1.val)
        while(l2.next):
            s2 += str(l2.val)
            l2 = l2.next
        s2 += str(l2.val)
        sumReversed = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        
        cur = head = ListNode(0)
        for char in sumReversed:
            cur.next = ListNode(char)
            cur = cur.next
        return head.next