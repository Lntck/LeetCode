class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        ptr = result
        while list1 and list2:
            if list1.val >= list2.val:
                ptr.next = list2
                list2 = list2.next
            else:
                ptr.next = list1
                list1 = list1.next
            ptr = ptr.next
        ptr.next = list1 if list1 else list2
        return result.next
