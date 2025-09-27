class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # simple approach using two separate lists
    # def partition(self, head: ListNode, x: int) -> ListNode:
    #     less_head = ListNode(0)
    #     less = less_head

    #     greater_or_equal_head = ListNode(0)
    #     greater = greater_or_equal_head

    #     while head:
    #         if head.val < x:
    #             less.next = head
    #             less = less.next
    #         else:
    #             greater.next = head
    #             greater = greater.next
    #         head = head.next
        
    #     less.next = greater_or_equal_head.next
    #     greater.next = None
    #     return less_head.next

    # Advanced in-place solution
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0, head)
        # start - last node in the <x partition
        start = dummy
        curr = dummy
        
        while curr.next:
            if curr.next.val < x:
                # save the node to be moved
                less = curr.next
                # skip over less in its original position
                curr.next = curr.next.next
                
                # save the node that was after start
                after_start = start.next
                # insert less-node right after start
                start.next = less
                # move start to the new last node in <x partition
                start = start.next
                # after less-node put what was originally after start
                start.next = after_start
                
                # move curr to start to continue checking from the new position
                curr = start
            else:
                curr = curr.next
        return dummy.next
