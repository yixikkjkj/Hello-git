# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        overflow = 0
        header = ListNode(0)
        p3 = header
        while p1 or p2 or overflow:
            v1, v2 = 0, 0
            if p1:
                v1 = p1.val
                p1 = p1.next
            if p2:
                v2 = p2.val
                p2 = p2.next
            val = v1 + v2 + overflow
            overflow = int(val / 10)
            val = val % 10
            target = ListNode(val)
            header.next = target
            header = target

        return p3.next


if __name__ == "__main__":
    li1 = ListNode(2)
    header = li1
    header.next = ListNode(4)
    header = header.next
    header.next = ListNode(3)
    header = header.next

    li2 = ListNode(5)
    header = li2
    header.next = ListNode(6)
    header = header.next
    header.next = ListNode(4)
    header = header.next

    sol = Solution()

    sol.addTwoNumbers(li1, li2)
