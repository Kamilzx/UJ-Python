# Kamil Nowak, Grupa 2
# 02.12.2022r.
# Python 2022/2023
# test_rectangles.py

import pytest
from rectangles import Rectangle
from points import Point

def test_center():
    assert Rectangle(0, 0, 2, 2).center() == Point(1, 1)
    
def test_from_points():
    rectangle = Rectangle.from_points((Point(2, 3), Point(6, 10)))
    assert str(rectangle) == '[(2, 3), (6, 10)]'

def test_size_get():
    rect = Rectangle(2, 3, 6, 10)
    assert rect.height == 7
    assert rect.width == 4
    assert rect.top == 10
    assert rect.bottom == 3
    assert rect.left == 2
    assert rect.right == 6

def test_point_get():
    p1 = Point(1, 2)
    p2 = Point(4, 5)
    rect = Rectangle.from_points((p1, p2))

    assert rect.bottomleft == p1
    
    assert rect.topright == p2
    
    assert rect.topleft == Point(p1.x, p2.y)
    
    assert rect.bottomright == Point(p2.x, p1.y)

if __name__ == "__main__":
    pytest.main()
    
#================================ test session starts =========================
#platform win32 -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
#rootdir: C:\Users\Kamil\Desktop\Studia\Python\zestaw8
#collected 4 items
#
#test_rectangles.py ....                                                       [100%]
#
#=============================== 4 passed in 0.04s ============================ 