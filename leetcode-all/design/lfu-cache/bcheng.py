class Node:
    def __init__(self, key, value):
        self.pre = None
        self.nxt = None
        self.key = key
        self.value = value
        self.freq = 0


class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node

    def append(self, node):
        node.pre = self.tail
        if self.tail is not None:
            self.tail.nxt = node
        self.tail = node

    def remove(self, node):
        if node.pre is not None:
            node.pre.nxt = node.nxt
        if node.nxt is not None:
            node.nxt.pre = node.pre
        if node is self.head:
            self.head = node.nxt
        if node is self.tail:
            self.tail = node.pre
        node.pre = node.nxt = None

    def __str__(self):
        res = []
        cur = self.head
        while cur is not None:
            res.append(cur.key)
            cur = cur.nxt
        return str(res)


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.data = {}
        self.capacity = capacity
        self.size = 0
        self.min_freq = 1

    def increment(self, node):
        if node.freq > 0:
            self.delete(node)
            if node.freq == self.min_freq:
                if node.freq not in self.data:
                    self.min_freq += 1
        node.freq += 1
        if node.freq not in self.data:
            self.data[node.freq] = LinkedList(node)
        else:
            self.data[node.freq].append(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.increment(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        node = self.cache.get(key)
        if node is None:
            node = Node(key, value)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                min_list = self.data[self.min_freq]
                deleted = min_list.head
                self.delete(deleted)
                self.cache.pop(deleted.key)
                self.size -= 1
            self.min_freq = 1
        else:
            node.value = value
        self.increment(node)

    def delete(self, node):
        linked = self.data[node.freq]
        linked.remove(node)
        if linked.head is None:
            self.data.pop(node.freq)


a = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
b = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
expected = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12,
            None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None,
            None, 18, None, None, None, None, 14, None, None, 18, None, None, 11, None, None, None, None, None, 18,
            None, None, -1, None, 4, 29, 30, None, 12, 11, None, None, None, None, 29, None, None, None, None, 17, -1,
            18, None, None, None, -1, None, None, None, 20, None, None, None, 29, 18, 18, None, None, None, None, 20,
            None, None, None, None, None, None, None]
obj = LFUCache(*b[0])
no = 0
for i, j, k in zip(a[1:], b[1:], expected[1:]):
    no += 1
    print(no, i, j)
    assert k == obj.__getattribute__(i)(*j)
    assert obj.min_freq == min(obj.data.keys())
