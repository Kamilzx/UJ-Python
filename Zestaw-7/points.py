# Kamil Nowak, Grupa 2
# 27.11.2022r.
# Python 2022/2023
# points.py


# ZADANIE 6.2 (KLASA POINT)
# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. 
# Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). 
# Napisać kod testujący moduł points.


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""
    
    def __init__(self, x=0, y=0):     # konstruktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):        # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        import math
        return math.sqrt(self.x*self.x + self.y*self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    def setUp(self):
        self.p1=Point(0, 1)
        self.p2=Point(1, 0)
        self.p3=Point(3, 4)
        self.p4=Point(2, 5)

    def test_str(self):
        self.assertEqual(self.p1.__str__(), "(0, 1)")

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), "Point(0, 1)")

    def test_eq(self):
        self.assertEqual(self.p1 == self.p2, False)
        self.assertEqual(self.p1 == self.p1, True)

    def test_ne(self):
        self.assertEqual(self.p1 != self.p1, False)
        self.assertEqual(self.p1 != self.p2, True)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(1, 1))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-1, 1))

    def test_mul(self):
        self.assertEqual(self.p3 * self.p4, 26)
        self.assertEqual(self.p1 * self.p2, 0)

    def test_cross(self):
        self.assertEqual(Point.cross(self.p3, self.p4), 7)
        
    def test__hash__(self):
        self.assertEqual(self.p1.__hash__(), self.p1.__hash__())
        
    def test_length(self):
        self.assertEqual(self.p1.length(), 1)
        self.assertEqual(self.p3.length(), 5)
  


if __name__=='__main__':
	unittest.main()

#test__hash__ (__main__.TestPoint) ... ok
#test_add (__main__.TestPoint) ... ok
#test_cross (__main__.TestPoint) ... ok
#test_eq (__main__.TestPoint) ... ok
#test_length (__main__.TestPoint) ... ok
#test_mul (__main__.TestPoint) ... ok
#test_ne (__main__.TestPoint) ... ok
#test_repr (__main__.TestPoint) ... ok
#test_str (__main__.TestPoint) ... ok
#test_sub (__main__.TestPoint) ... ok
#
#----------------------------------------------------------------------
#Ran 10 tests in 0.003s
#
#OK