class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(key=-10086, val=-10086)
        self.dummy_tail = ListNode(key=10086, val=10086)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.node_cnt = 0

    def _add_to_head(self, node):
        original_body = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = original_body
        original_body.prev = node

    def add_to_head(self, node):
        self._add_to_head(node)
        self.node_cnt += 1

    def move_to_head(self, node):
        self._add_to_head(node)

    def remove_tail(self) -> ListNode:
        if self.node_cnt < 1:
            raise Exception('Empty ListNode! Cannot remove tail!')
        node_to_remove = self.dummy_tail.prev
        original_body = self.dummy_tail.prev.prev
        original_body.next = self.dummy_tail
        self.dummy_tail.prev = original_body
        self.node_cnt -= 1
        return node_to_remove

    def remove(self, node: ListNode):
        node.prev.next, node.next.prev = node.next, node.prev
        self.node_cnt -= 1
        return node

    def debug_print_list(self):
        ret = []
        p = self.dummy_head
        while p:
            ret.append(p.key)
            p = p.next
        return ret


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_table = {}  # key: int, val: ListNode
        self.freq_table = {}  # key: int, val: DoubleLinkedList
        self.size = 0
        self.min_freq = 0

    def get(self, key: int) -> int:
        # edge case: self.capacity == 0
        if self.capacity == 0:
            return -1

        # update freq cnt
        # move node from self.freq_table[freq + 1]
        node = self.key_table.get(key, None)
        if node is None:
            return -1

        original_freq = node.freq
        node.freq += 1

        self.remove_from_freq_table(original_freq, node)
        self.add_to_freq_table(node.freq, node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # edge case: self.capacity == 0
        if self.capacity == 0:
            return

        node = self.key_table.get(key, None)
        if node is None:
            # delete node to free capacity if reaches capacity
            # create a new node in self.key_table
            # self.min_freq = 1
            # insert into self.freq_table[self.min_freq] if there is a linked list else create a new one
            # increment self.size
            self.delete_node_to_free_capacity()
            self.min_freq = 1
            node = ListNode(key=key, val=value)
            self.key_table[key] = node
            self.add_to_freq_table(self.min_freq, node)
            self.size += 1

        else:
            # update node.val and node.freq
            # move node to freq_table[freq + 1]
            # update self.min_freq if original node.freq == self.min_freq
            original_freq = node.freq

            node.val = value
            node.freq += 1

            self.remove_from_freq_table(original_freq, node)
            self.add_to_freq_table(node.freq, node)

    def remove_from_freq_table(self, freq: int, node: ListNode) -> None:
        linked_list = self.freq_table.get(freq)
        if linked_list.node_cnt == 1:
            self.freq_table.pop(freq)
        else:
            linked_list.remove(node)
        self.update_min_freq(freq)

    def add_to_freq_table(self, freq: int, node: ListNode) -> None:
        linked_list = self.freq_table.get(freq, None)
        if linked_list:
            linked_list.add_to_head(node)
        else:
            linked_list = DoubleLinkedList()
            linked_list.add_to_head(node)
            self.freq_table[freq] = linked_list

    def update_min_freq(self, original_freq):
        if original_freq == self.min_freq:
            if self.freq_table.get(self.min_freq) is None:
                self.min_freq += 1

    def delete_node_to_free_capacity(self):
        # if we reach capacity, delete LFU node
        # remove least frequently used node. which is the tail in freq_table[min_freq]
        # pop node_removed from self.key_table too
        if self.size == self.capacity:
            linked_list = self.freq_table[self.min_freq]
            node_removed = linked_list.remove_tail()

            self.key_table.pop(node_removed.key)
            self.size -= 1

# test cases
if __name__ == '__main__':
    # test 1 capacity = 0
    cache = LFUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1

    cache.put(2, 2)
    assert cache.get(2) == -1

    # test 2
    # ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    cache = LFUCache(2)
    cache.put(1, 1)
    assert list(cache.freq_table.keys()) == [1]
    assert list(cache.key_table.keys()) == [1]
    node = cache.key_table[1]
    assert node.key == 1
    assert node.val == 1
    assert node.freq == 1
    linked_list = cache.freq_table[1]
    assert linked_list.node_cnt == 1
    assert cache.min_freq == 1

    cache.put(2, 2)
    assert set(list(cache.freq_table.keys())) == {1}
    assert set(list(cache.key_table.keys())) == {1, 2}
    node = cache.key_table[2]
    assert node.key == 2
    assert node.val == 2
    assert node.freq == 1
    linked_list = cache.freq_table[1]
    assert linked_list.node_cnt == 2
    assert cache.min_freq == 1

    ans = cache.get(1)
    assert ans == 1
    assert set(list(cache.freq_table.keys())) == {1, 2}
    assert set(list(cache.key_table.keys())) == {1, 2}
    node = cache.key_table[1]
    assert node.key == 1
    assert node.val == 1
    assert node.freq == 2
    node = cache.key_table[2]
    assert node.key == 2
    assert node.val == 2
    assert node.freq == 1
    linked_list = cache.freq_table[1]
    assert linked_list is not None
    assert linked_list.node_cnt == 1
    linked_list = cache.freq_table[2]
    assert linked_list is not None
    assert linked_list.node_cnt == 1
    assert linked_list.dummy_head.next.key == 1

    cache.put(3, 3)
    assert set(list(cache.freq_table.keys())) == {1, 2}
    assert set(list(cache.key_table.keys())) == {1, 3}
    assert cache.min_freq == 1
    freq_1 = cache.freq_table[1]
    assert freq_1.debug_print_list() == [-10086, 3, 10086]
    freq_2 = cache.freq_table[2]
    assert freq_2.debug_print_list() == [-10086, 1, 10086]
    assert cache.min_freq == 1

    ans = cache.get(2)
    assert ans == -1

    ans = cache.get(3)
    assert ans == 3
    assert set(list(cache.freq_table.keys())) == {2}
    assert set(list(cache.key_table.keys())) == {1, 3}
    assert cache.min_freq == 2
    freq_2 = cache.freq_table[2]
    assert freq_2.debug_print_list() == [-10086, 3, 1, 10086]

    cache.put(4, 4)
    assert set(list(cache.freq_table.keys())) == {1, 2}
    assert set(list(cache.key_table.keys())) == {3, 4}
    assert cache.min_freq == 1
    freq_1 = cache.freq_table[1]
    assert freq_1.debug_print_list() == [-10086, 4, 10086]

    assert cache.get(1) == -1

    assert cache.get(3) == 3
    assert set(list(cache.freq_table.keys())) == {1, 3}
    assert set(list(cache.key_table.keys())) == {3, 4}
    assert cache.min_freq == 1

    assert cache.get(4) == 4
    assert set(list(cache.freq_table.keys())) == {2, 3}
    assert set(list(cache.key_table.keys())) == {3, 4}
    assert cache.min_freq == 2

    # test 3
    # ["LFUCache", "get", "put", "get", "put", "put", "get", "get"]
    # [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
    cache = LFUCache(2)
    cache.put(2, 6)
    cache.put(1, 5)
    cache.put(1, 2)
    assert cache.get(1) == 2
    assert cache.get(2) == 6