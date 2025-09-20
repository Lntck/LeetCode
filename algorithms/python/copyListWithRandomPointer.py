class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head: return None
        hashmap = {}

        # initialize all nodes in the hashmap using {old: new} (without next and random)
        dummy = head
        while dummy:
            hashmap[dummy] = Node(dummy.val)
            dummy = dummy.next
        
        # using a hashmap, add the next and random information to the new nodes
        dummy = head
        while dummy:
            hashmap[dummy].next = hashmap.get(dummy.next)
            hashmap[dummy].random = hashmap.get(dummy.random)
            dummy = dummy.next
        return hashmap[head]
