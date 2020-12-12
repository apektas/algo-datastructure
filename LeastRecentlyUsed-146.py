class DLL:
    def __init__(self, key:int, val: int, next: DLL = None, prev: DLL = None ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.dict = dict()
        self.head = DLL(0,0) # most recently used one
        self.tail = DLL(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLL) -> None:
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


    def _addTop(self, node):
        head = self.head.next
        node.next = head
        head.prev = node
        node.prev = self.head

        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            # remove from the list then add Top
            self._remove(node)
            self._addTop(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # move to node to tail
            node = self.dict[key]
            # update its value
            node.val = value

            self._remove(node)
            self._addTop(node)
            return

        node = DLL(key=key, val=value)
        self.dict[key] = node
        self._addTop(node)

        if len(self.dict) > self.capacity:
            tail = self.tail.prev
            self._remove(tail)
            del self.dict[tail.key]
