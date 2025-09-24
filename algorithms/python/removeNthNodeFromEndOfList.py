class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        before_del_node, curr = dummy, head
        while curr:
            if n == 0:
                before_del_node = before_del_node.next
            else:
                n -= 1
            curr = curr.next
        
        before_del_node.next = before_del_node.next.next
        return dummy.next
