# Kamil Nowak, Grupa 2
# 08.12.2022r.
# Python 2022/2023
# stack.py

import unittest

class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []
        
    def __str__(self):                  # podglądamy stos
        return str(self.items)
    
    def is_empty(self):
        return not self.items
    
    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if len(self.items) == self.size:
            raise OverflowError("Stos jest pełny")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty")
        return self.items.pop()

# Testy jednostkowe dla klasy Stack
class TestStack(unittest.TestCase):
    def test_overflow(self):
        stack = Stack(10)
        with self.assertRaises(OverflowError):
            for i in range(11):
                stack.push(i)

    def test_underflow(self):
        stack = Stack(10)
        with self.assertRaises(IndexError):
            for i in range(11):
                stack.pop()

if __name__ == "__main__":
    unittest.main()
    
#PS C:\Users\Kamil\Desktop\Studia\Python> python3 stack.py -v      
#test_overflow (__main__.TestStack) ... ok
#test_underflow (__main__.TestStack) ... ok
#
#----------------------------------------------------------------------
#Ran 2 tests in 0.001s
#
#OK