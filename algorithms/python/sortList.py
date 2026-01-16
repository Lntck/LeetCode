class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def split(head: ListNode | None, size: int) -> tuple[ListNode | None, ListNode | None]:
            current = head
            for _ in range(size - 1):
                if not current: break
                current = current.next
            
            if not current: return head, None

            next_part = current.next
            current.next = None
            return head, next_part


        def merge(left: ListNode | None, right: ListNode | None) -> tuple[ListNode | None, ListNode | None]:
            dummy = ListNode(0)
            cur = dummy
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            cur.next = left if left else right

            while cur.next:
                cur = cur.next

            return dummy.next, cur

        n = 0
        cur = head
        while cur:
           n += 1
           cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        size = 1
        while size < n:
            previous = dummy
            current = dummy.next

            while current:
                part1, next_part = split(current, size)
                part2, current = split(next_part, size)

                merged_head, merged_tail = merge(part1, part2)
                if merged_head is not None and merged_tail is not None:
                    previous.next = merged_head
                    previous = merged_tail
            size *= 2
        return dummy.next
