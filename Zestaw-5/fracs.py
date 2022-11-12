# Kamil Nowak, Grupa 2
# 12.11.2022r.
# Python 2022/2023
# fracs.py


# Zadanie 5.2
# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. 
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. 
# Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.


def add_frac(frac1, frac2):         # frac1 + frac2
    res = [1,1]
    res[0] = frac1[0]*frac2[1]+frac2[0]*frac1[1]
    res[1] = frac1[1]*frac2[1]
    return fracNWD(res)
def sub_frac(frac1, frac2):         # frac1 - frac2
    res = [1,1]
    res[0] = frac1[0]*frac2[1]-frac2[0]*frac1[1]
    res[1] = frac1[1]*frac2[1]
    return fracNWD(res)

def mul_frac(frac1, frac2):         # frac1 * frac2
    res = [1,1]
    res[0] = frac1[0]*frac2[0]
    res[1] = frac1[1]*frac2[1]
    return fracNWD(res)
    
def div_frac(frac1, frac2):         # frac1 / frac2
    frac2[0], frac2[1] = frac2[1], frac2[0]
    return mul_frac(frac1,frac2)

def is_positive(frac):              # bool, czy dodatni
    if frac[0] * frac[1] = 0: 
        return True
    else: 
        return False

def is_zero(frac):                  # bool, typu [0, x]
    if frac[0] == 0: 
        return True
    else: 
        return False

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    if frac2float(frac1) > frac2float(frac2):
        return -1
    elif frac2float(frac1) < frac2float(frac2):
        return 1
    else:
        return 0

def frac2float(frac):               # konwersja do float
    return (float(float(frac[0])/float(frac[1])))

def fracNWD(frac):
    res = [1,1]
    nwd = func_nwd(frac[0],frac[1])
    res[0] = frac[0]/nwd
    res[1] = frac[1]/nwd
    return res
    
def func_nwd(a, b):
    if b > 0:
        return func_nwd(b, a%b)
    else:
        return a

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)



import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 2], [1, 3]), [1, 3])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 1], [1, 2]), [4, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([-2, 5]), False)
        self.assertEqual(is_positive([2, 5]), True)
        self.assertEqual(is_positive([-2, -5]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([2, 1]), False)
        self.assertEqual(is_zero([0, 4]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([2, 1],[1, 5]), -1)
        self.assertEqual(cmp_frac([2, 2],[4, 4]), 0)
        self.assertEqual(cmp_frac([0, 1],[1, 5]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([2, 1]), 2.00)
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([1, 5]), 0.20)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    
    

#test_add_frac (__main__.TestFractions) ... ok
#test_cmp_frac (__main__.TestFractions) ... ok
#test_div_frac (__main__.TestFractions) ... ok
#test_frac2float (__main__.TestFractions) ... ok
#test_is_positive (__main__.TestFractions) ... ok
#test_is_zero (__main__.TestFractions) ... ok
#test_mul_frac (__main__.TestFractions) ... ok
#test_sub_frac (__main__.TestFractions) ... ok
#
#----------------------------------------------------------------------
#Ran 8 tests in 0.003s
#
#OK
