# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n: int):
        p1 = head
        for _ in range(n):
            p1 = p1.next
            if not p1:
                return head.next
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next

        if n == 1:
            p2.next = None
        else:
            # 删除 p2 的下一个
            p2.next = p2.next.next
        return head
