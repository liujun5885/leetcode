class DoubleLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.cache = dict()
       self.dummy_head = DoubleLinkedListNode(-10086, -10086)
       self.dummy_tail = DoubleLinkedListNode(-10086, -10086)
       self.dummy_head.next = self.dummy_tail
       self.dummy_tail.prev = self.dummy_head

    @property
    def size(self):
        return len(self.cache)

    def get(self, key: int) -> int:
        print(self.cache)
        if key not in self.cache.keys():
            return -1
        
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = DoubleLinkedListNode(key=key, val=value)
            self.cache[key] = node
            self.add_to_head(node)
            if self.size > self.capacity:
                # remove tail
                # remove key from self.cache
                node = self.remove_tail()
                self.cache.pop(node.key)

    def move_to_head(self, node: DoubleLinkedListNode):
        if node.prev == self.dummy_head:
            return
        original_head = self.dummy_head.next
        original_tail = node.next
        node.prev.next = original_tail
        original_tail.prev = node.prev
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = original_head
        original_head.prev = node
        # original_head.next = original_tail
        # original_head.prev = node
        # original_tail.prev = original_first
    
    def add_to_head(self, node: DoubleLinkedListNode):
        original_first = self.dummy_head.next
        self.dummy_head.next = node
        node.next = original_first
        node.prev = self.dummy_head
        original_first.prev = node
    
    def remove_tail(self):
        tail = self.dummy_tail.prev
        tail.prev.next = self.dummy_tail
        self.dummy_tail.prev = tail.prev
        return tail

    def print_linked_list(self):
        h = self.dummy_head
        output = []
        while h:
            output.append(h.val)
            h = h.next
        print(f'linked list is {output}')
        return output


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
for i in range(1, 5):
    obj.put(i, i)
assert obj.print_linked_list() == [-10086, 4, 3, 2, -10086]

for i in reversed(range(2, 5)):
    assert obj.get(i) == i
assert obj.get(1) == -1

obj.put(5, 5)
print(obj.print_linked_list())
assert obj.print_linked_list() == [-10086, 5, 4, 3, -10086]

assert obj.get(1) == -1
assert obj.get(2) == -1
assert obj.get(3) == 3
assert obj.get(4) == 4
assert obj.get(5) == 5
