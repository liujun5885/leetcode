import heapq


class MaxHeap:
    def __init__(self, data=None):
        self.data = data or []

    def size(self):
        return self.data.__len__()

    def push(self, value):
        return heapq.heappush(self.data, -value)

    def pop(self):
        return -heapq.heappop(self.data)

    def top(self):
        return -self.data[0]


class MinHeap:
    def __init__(self, data=None):
        self.data = data or []

    def size(self):
        return self.data.__len__()

    def push(self, value):
        return heapq.heappush(self.data, value)

    def pop(self):
        return heapq.heappop(self.data)

    def top(self):
        return self.data[0]


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = MaxHeap()
        self.bigger = MinHeap()

    def addNum(self, num: int) -> None:
        self.smaller.push(num)
        self.bigger.push(self.smaller.pop())
        if self.bigger.size() > self.smaller.size():
            self.smaller.push(self.bigger.pop())

    def findMedian(self) -> float:
        if self.smaller.size() > self.bigger.size():
            return self.smaller.top()
        else:
            return (self.smaller.top() + self.bigger.top()) / 2
