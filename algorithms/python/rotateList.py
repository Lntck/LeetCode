class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head

        # calculate list length and find the tail node in one pass
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        
        k %= n
        if k == 0: return head

        dummy = ListNode(0, head)
        curr = dummy
        # Move to the node that will become the new tail
        for _ in range(n - k):
            curr = curr.next

        # new head becomes the node after curr-(new tail)
        dummy.next = curr.next
        # original tail connects to original head
        tail.next = head
        # curr becomes new tail
        curr.next = None

        return dummy.next
