class DoubleListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DoubleListNode) -> None:
        prev_tail = self.tail.prev

        prev_tail.next = node
        node.prev = prev_tail

        node.next = self.tail
        self.tail.prev = node
    
    def _remove_node(self, node: DoubleListNode) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_end(self, node: DoubleListNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self._move_to_end(self.hashmap[key])
            return self.hashmap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            updated_node = self.hashmap[key]
            updated_node.val = value
            self._move_to_end(updated_node)
        else:
            if len(self.hashmap) >= self.capacity:
                lru_node = self.head.next

                self._remove_node(lru_node)
                del self.hashmap[lru_node.key]
            
            self.hashmap[key] = DoubleListNode(key, value)
            self._add_node(self.hashmap[key])
