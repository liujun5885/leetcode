from typing import List
import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Union Find. 
        1. Initially each num has no connection. 
        2. In the main function, connect num with num - 1 if num - 1 exists.
        3. Iterate graph and find each time to do a final round of path compression
        3. Count the max occurrence of parent
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(nums) < 2:
            return len(nums)
        self.graph = {num: num for num in nums}
        for num in nums:
            self.union(num, num - 1)
        for g in self.graph:
            self.find(g)
        return max(collections.Counter(self.graph.values()).values())

    def find(self, x: int) -> int:
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])
        return self.graph[x]

    def union(self, x: int, y: int) -> None:
        if not (x in self.graph and y in self.graph):
            return
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.graph[py] = px


if __name__ == '__main__':
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert Solution().longestConsecutive([]) == 0
    assert Solution().longestConsecutive([1]) == 1
    assert Solution().longestConsecutive([4, 0]) == 1