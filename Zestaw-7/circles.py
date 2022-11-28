# Kamil Nowak, Grupa 2
# 27.11.2022r.
# Python 2022/2023
# circles.py


# ZADANIE 7.5 (KLASA CIRCLE)

# W pliku circles.py zdefiniować klasę Circle wraz z potrzebnymi metodami. 
# Okrąg jest określony przez podanie środka i promienia. 
# Wykorzystać wyjątek ValueError do obsługi błędów. 
# Napisać kod testujący moduł circles.


from points import Point
import math

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):            # "Circle(x, y, radius)"
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return (self.pt == other.pt) and (self.radius == other.radius)

    def __ne__(self, other):
        return not self == other

    def area(self): 	           # pole powierzchni
        return math.pi*(self.radius**2)

    def move(self, x, y):          # przesuniecie o (x, y)
        self.pt += Point(x, y)

    def cover(self, other):        # najmniejszy okrąg pokrywający oba
        import math
        srodek = Point((self.pt.x + other.pt.x)/2, (self.pt.y + other.pt.y)/2)
        radius_base = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)/2
        radius_add = max(self.radius, other.radius)
        return Circle(srodek.x, srodek.y, (radius_base + radius_add))


# testing

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(1, 1, 1)
        self.c2 = Circle(1, 2, 1)
        self.c3 = Circle(4, 4, 2)

    def test_repr(self):
        self.assertEqual(self.c1.__repr__(), "Circle(1, 1, 1)") 

    def test_area(self):
        self.assertEqual(self.c1.area(), math.pi)

    def test_move(self):
        self.c1.move(1, 1)
        self.assertEqual((self.c1 == Circle(2, 2, 1)), True)

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c2), Circle(1, 1.5, 1.5))

if __name__ == '__main__':
    unittest.main()
    
#test_area (__main__.TestCircle) ... ok
#test_cover (__main__.TestCircle) ... ok
#test_move (__main__.TestCircle) ... ok
#test_repr (__main__.TestCircle) ... ok
#
#----------------------------------------------------------------------
#Ran 4 tests in 0.001s
#
#OK