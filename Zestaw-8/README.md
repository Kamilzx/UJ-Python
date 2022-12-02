# **Zadania**

OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie

### **ZADANIE 8.1 (KLASA RECTANGLE)**
Wzbogacić klasę Rectangle o nowe funkcjonalności (plik rectangles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć prostokąt z listy lub krotki zawierającej dwa punkty, lewy dolny i prawy górny. Wywołanie:
rectangle = Rectangle.from_points((point1, point2))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. 

Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Można rozważyć zamianę metody center() na atrybut wirtualny.

W osobnym pliku (test_rectangles.py) przygotować testy klasy Rectangle w formacie dla modułu 'pytest'.