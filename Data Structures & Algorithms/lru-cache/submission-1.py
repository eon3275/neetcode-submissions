class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    def _add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
        if len(self.cache)>self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
        
