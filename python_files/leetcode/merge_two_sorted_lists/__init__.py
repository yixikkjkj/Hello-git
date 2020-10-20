# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p1 = l1
        p2 = l2
        if l1.val <= l2.val:
            rlt = ListNode(l1.val)
            p1 = p1.next
        else:
            rlt = ListNode(l2.val)
            p2 = p2.next
        rlt_header = rlt
        while p1 and p2:
            if p1.val <= p2.val:
                rlt.next = ListNode(p1.val)
                p1 = p1.next
            else:
                rlt.next = ListNode(p2.val)
                p2 = p2.next
            rlt = rlt.next

        if p1:
            rlt.next = p1
        if p2:
            rlt.next = p2
        return rlt_header
