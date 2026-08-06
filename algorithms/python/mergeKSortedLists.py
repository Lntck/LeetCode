class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists: return None

        def merge_two(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            start = ListNode()
            dummy = start
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            dummy.next = l1 if l1 else l2
            return start.next

        def divide_and_conquer(st: int, end: int):
            length = end - st + 1
            if length == 1:
                return lists[end]
            left = divide_and_conquer(st, st + ((length - 1) // 2))
            right = divide_and_conquer(st + ((length - 1) // 2) + 1, end)
            return merge_two(left, right)

        return divide_and_conquer(0, len(lists) - 1)
