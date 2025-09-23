class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        dummy = ListNode(0)
        dummy.next = head

        prev_group_end = dummy
        for _ in range(n // k):
            group_head = prev_group_end.next
            curr, prev_node = group_head, None
            for _ in range(k):
                tmp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = tmp

            group_head.next = curr
            prev_group_end.next = prev_node
            prev_group_end = group_head
        return dummy.next
