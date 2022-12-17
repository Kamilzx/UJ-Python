# Kamil Nowak, Grupa 2
# 18.12.2022r.
# Python 2022/2023
# randomqueue.py

import random
from collections import deque

class RandomQueue:
    def __init__(self):
        self.queue = deque()

    def insert(self, item):
        return self.queue.append(item)

    def remove(self):
        # losujemy czy chcemy usunac tail czy head
        index = random.randint(0, 1)
        if index == 1:
            return self.queue.pop()
        else:
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        # w naszym przypadku kolejka nigdy nie jest pełna
        return False

    def clear(self):
        self.queue = deque()



import unittest

class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()

    def test_insert(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)

        self.assertEqual(self.queue.queue, deque([1, 2, 3]))

    def test_remove(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)

        self.assertIn(self.queue.remove(), deque([1, 2, 3]))
        self.assertIn(self.queue.remove(), deque([1, 2, 3]))
        self.assertIn(self.queue.remove(), deque([1, 2, 3]))

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

        self.queue.insert(1)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())

    def test_clear(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)
        self.queue.clear()

        self.assertTrue(self.queue.is_empty())

if __name__ == "__main__":
    unittest.main()
    
#PS C:\Users\Kamil\Desktop\Studia\Python> python3 randomqueue.py -v
#test_clear (__main__.TestRandomQueue) ... ok
#test_insert (__main__.TestRandomQueue) ... ok
#test_is_empty (__main__.TestRandomQueue) ... ok
#test_is_full (__main__.TestRandomQueue) ... ok
#test_remove (__main__.TestRandomQueue) ... ok
#
#----------------------------------------------------------------------
#Ran 5 tests in 0.001s
#
#OK