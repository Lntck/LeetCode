class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        
        dummy = head
        for i in range((n) // 2):
            dummy = dummy.next
        cur = dummy.next
        dummy.next = None

        tail = None
        while cur:
            temp = cur.next
            cur.next = tail
            tail = cur
            cur = temp

        dummy = head
        while tail:
            temp = dummy.next
            temp2 = tail.next
            dummy.next = tail
            tail.next = temp
            tail = temp2
            dummy = temp      
