# https://leetcode-cn.com/problems/task-scheduler/

from typing import List
from unittest import TestCase
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_tasks = max(task_counter.values())
        tasks_with_max_number = sum([1 for k, v in task_counter.items() if v == max_tasks])
        return max((max_tasks - 1) * (n + 1) + tasks_with_max_number, len(tasks))


class TestCases(TestCase):
    def test_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        actual = Solution().leastInterval(tasks, n)
        self.assertEqual(expected, actual)

    def test_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        actual = Solution().leastInterval(tasks, n)
        self.assertEqual(expected, actual)

    def test_3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        actual = Solution().leastInterval(tasks, n)
        self.assertEqual(expected, actual)
