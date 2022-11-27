# Kamil Nowak, Grupa 2
# 27.11.2022r.
# Python 2022/2023
# fracs.py


# ZADANIE 6.5 (KLASA FRAC)
# W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami. 
# Ułamek jest reprezentowany przez parę liczb całkowitych. 
# Napisać kod testujący moduł fracs.

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return str(self.x)+"/"+str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac("+str(self.x)+","+str(self.y)+")"

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):    # Py2.7 i Py3
        res1 = Frac.fracNWD(self)
        res2 = Frac.fracNWD(other)
        return (res1.x == res2.x) and (res1.y == res2.y)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y
        other.y *= self.y
        return (self.x < other.x)

    def __le__(self, other):
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y
        other.y *= self.y
        return (self.x <= other.x)

    def __gt__(self, other):
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y
        other.y *= self.y
        return (self.x > other.x)

    def __ge__(self, other):
        self.x *= other.y
        other.x *= self.y
        self.y *= other.y
        other.y *= self.y
        return (self.x >= other.x)

    def __add__(self, other):  # frac1 + frac2
        res = Frac(1,1)
        res.x = self.x*other.y+other.x*self.y
        res.y = self.y*other.y
        return Frac.fracNWD(res)

    def __sub__(self, other):  # frac1 - frac2
        res = Frac(1,1)
        res.x = self.x*other.y-other.x*self.y
        res.y = self.y*other.y
        return Frac.fracNWD(res)

    def __mul__(self, other):  # frac1 * frac2
        res = Frac(1,1)
        res.x = self.x*other.x
        res.y = self.y*other.y
        return Frac.fracNWD(res)

    def __div__(self, other):  # frac1 / frac2, Py2
        other.x, other.y = other.y, other.x
        return Frac.__mul__(self, other)

    def __truediv__(self, other):  # frac1 / frac2, Py3
        other.x, other.y = other.y, other.x
        return Frac.__mul__(self, other)

    #def __floordiv__(self, other): pass  # frac1 // frac2, opcjonalnie

    #def __mod__(self, other): pass  # frac1 % frac2, opcjonalnie
     
    def fracNWD(self):
        res = Frac(1,1)
        nwd = Frac.func_nwd(self.x,self.y)
        res.x = self.x/nwd
        res.y = self.y/nwd
        return res   
    
    def func_nwd(a, b):
        if b > 0:
            return Frac.func_nwd(b, a%b)
        else:
            return a
        
    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return (float(float(self.x)/float(self.y)))

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])



# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(0, 1)
        self.frac2 = Frac(1, 3)
        self.frac3 = Frac(1, 2)
        self.frac4 = Frac(-3, 4)
        self.frac5 = Frac(2, 6)
        
    def test__str__(self):
        self.assertEqual(self.frac1.__str__(), "0")
        self.assertEqual(self.frac2.__str__(), "1/3")
        self.assertEqual(self.frac3.__str__(), "1/2")
        self.assertEqual(self.frac4.__str__(), "-3/4")
        
    def test__repr__(self):
        self.assertEqual(self.frac1.__repr__(), "Frac(0,1)")
        self.assertEqual(self.frac2.__repr__(), "Frac(1,3)")
        self.assertEqual(self.frac3.__repr__(), "Frac(1,2)")
        self.assertEqual(self.frac4.__repr__(), "Frac(-3,4)")
        
    def test__eq__(self):
        self.assertEqual(self.frac2.__eq__(self.frac5), True)
        self.assertEqual(self.frac1.__eq__(self.frac3), False)
        
    def test__ne__(self):
        self.assertEqual(self.frac1.__ne__(self.frac1), False)
        self.assertEqual(self.frac1.__ne__(self.frac3), True)
        
    def test__lt__(self):
        self.assertEqual(self.frac1.__lt__(self.frac2), True)
        self.assertEqual(self.frac3.__lt__(self.frac2), False)
        
    def test__le__(self):
        self.assertEqual(self.frac2.__le__(self.frac5), True)
        self.assertEqual(self.frac1.__le__(self.frac4), False)
        
    def test__gt__(self):
        self.assertEqual(self.frac2.__gt__(self.frac1), True)
        self.assertEqual(self.frac2.__gt__(self.frac3), False)
        
    def test__ge__(self):
        self.assertEqual(self.frac5.__ge__(self.frac2), True)
        self.assertEqual(self.frac4.__ge__(self.frac1), False)
        
    def test__add__(self):
        self.assertEqual(self.frac1.__add__(self.frac2), Frac(1,3))
        self.assertEqual(self.frac3.__add__(self.frac4), Frac(-1,4))
        
    def test__sub__(self):
        self.assertEqual(self.frac1.__sub__(self.frac2), Frac(-1,3))
        self.assertEqual(self.frac3.__sub__(self.frac4), Frac(5,4))
        
    def test__mul__(self):
        self.assertEqual(self.frac1.__mul__(self.frac2), Frac(0,1))
        self.assertEqual(self.frac3.__mul__(self.frac4), Frac(-3,8))
        
    def test__div__(self):
        self.assertEqual(self.frac2.__div__(self.frac3), Frac(2,3))
        self.assertEqual(self.frac4.__div__(self.frac5), Frac(-9,4))
        
    def test__truediv__(self):
        self.assertEqual(self.frac2.__truediv__(self.frac3), Frac(2.0,3.0))
        self.assertEqual(self.frac4.__truediv__(self.frac5), Frac(-9,4))
        
    def test__pos__(self):
        self.assertEqual(self.frac5.__pos__(), Frac(2,6))
        
    def test__neg__(self):
        self.assertEqual(self.frac5.__neg__(), Frac(-2,6))
        
    def test__invert__(self):
        self.assertEqual(self.frac5.__invert__(), Frac(6,2))
        
    def test__float__(self):
        self.assertEqual(self.frac3.__float__(), 0.5)
        
    def test__hash__(self):
        self.assertEqual(self.frac1.__hash__(), self.frac1.__hash__())

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

#test__add__ (__main__.TestFrac) ... ok
#test__div__ (__main__.TestFrac) ... ok
#test__eq__ (__main__.TestFrac) ... ok
#test__float__ (__main__.TestFrac) ... ok
#test__ge__ (__main__.TestFrac) ... ok
#test__gt__ (__main__.TestFrac) ... ok
#test__hash__ (__main__.TestFrac) ... ok
#test__invert__ (__main__.TestFrac) ... ok
#test__le__ (__main__.TestFrac) ... ok
#test__lt__ (__main__.TestFrac) ... ok
#test__mul__ (__main__.TestFrac) ... ok
#test__ne__ (__main__.TestFrac) ... ok
#test__neg__ (__main__.TestFrac) ... ok
#test__pos__ (__main__.TestFrac) ... ok
#test__repr__ (__main__.TestFrac) ... ok
#test__str__ (__main__.TestFrac) ... ok
#test__sub__ (__main__.TestFrac) ... ok
#test__truediv__ (__main__.TestFrac) ... ok
#
#----------------------------------------------------------------------
#Ran 18 tests in 0.005s
#
#OK    
