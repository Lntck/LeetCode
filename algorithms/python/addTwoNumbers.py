class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        pointer_to_result = result
        remainder = 0

        while l1 or l2 or remainder:
            a, b = l1.val if l1 else 0, l2.val if l2 else 0

            pointer_to_result.next = ListNode(val=(a + b + remainder) % 10)
            remainder = (a + b + remainder) // 10

            pointer_to_result = pointer_to_result.next
            l1, l2= l1.next if l1 else l1, l2.next if l2 else l2
        return result.next
