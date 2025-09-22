class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Move prev to the node just before the reversal start position
        prev = dummy
        for _ in range(left-1):
            prev = prev.next

        next_node = None
        curr = prev.next
        tail = curr

        # Reverse the sublist from left to right
        for _ in range(right-left+1):
            tmp = curr.next
            curr.next = next_node
            next_node = curr
            curr = tmp
        
        # Connect the reversed portion back to the main list
        prev.next = next_node
        tail.next = curr

        return dummy.next
