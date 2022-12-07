# Kamil Nowak, Grupa 2
# 08.12.2022r.
# Python 2022/2023
# doublelist.py

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node   # stary head
            self.head = node        # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node   # stary tail
            self.tail = node        # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node
        
    def find_max(self): # W tej implementacji iterujemy przez wszystkie węzły w liście i sprawdzamy, 
                        # czy ich wartość jest większa od obecnego maksymalnego węzła. 
                        # Jeśli tak, to ustawiamy tę wartość jako nowy maksymalny węzeł. W końcu zwracamy maksymalny węzeł.
        if self.is_empty():
            return None

        current = self.head
        max_node = current
        while current:
            if current.data > max_node.data:
                max_node = current
            current = current.next

        return max_node
    
    def find_min(self):
        """Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy."""
        if self.is_empty():
            return None

        min_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.data < min_node.data:
                min_node = current_node
            current_node = current_node.next

        return min_node

    def remove(self, node):

        if self.is_empty():
            return None
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            if node is self.head:
                self.head = self.head.next
                self.head.prev = None   # czyszczenie
            elif node is self.tail:
                self.tail = self.tail.prev
                self.tail.next = None   # czyszczenie
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.length -= 1
            return node

    def clear(self):
        """Czyszczenie listy."""
        self.head = None
        self.tail = None
        self.length = 0



import unittest

class TestDoubleList(unittest.TestCase):
    def setUp(self):
        # Utworzenie pustej listy dwukierunkowej przed każdym testem.
        self.list = DoubleList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())

        node = Node(1)
        self.list.insert_head(node)

        self.assertFalse(self.list.is_empty())

    def test_count(self):
        self.assertEqual(self.list.count(), 0)

        node1 = Node(1)
        self.list.insert_head(node1)

        self.assertEqual(self.list.count(), 1)

        node2 = Node(2)
        self.list.insert_head(node2)

        self.assertEqual(self.list.count(), 2)

    def test_insert_head(self):
        node1 = Node(1)
        self.list.insert_head(node1)

        self.assertEqual(self.list.head, node1)
        self.assertEqual(self.list.tail, node1)

        node2 = Node(2)
        self.list.insert_head(node2)

        self.assertEqual(self.list.head, node2)
        self.assertEqual(self.list.tail, node1)

    def test_insert_tail(self):
        node1 = Node(1)
        self.list.insert_tail(node1)

        self.assertEqual(self.list.head, node1)
        self.assertEqual(self.list.tail, node1)

        node2 = Node(2)
        self.list.insert_tail(node2)

        self.assertEqual(self.list.head, node1)
        self.assertEqual(self.list.tail, node2)

    def test_remove_head(self):
        node1 = Node(1)
        self.list.insert_head(node1)

        node2 = Node(2)
        self.list.insert_head(node2)

        node3 = Node(3)
        self.list.insert_head(node3)

        self.assertEqual(self.list.remove_head(), node3)
        self.assertEqual(self.list.remove_head(), node2)
        self.assertEqual(self.list.remove_head(), node1)

        with self.assertRaises(ValueError):
            self.list.remove_head()
            
    def test_remove_tail(self):
        # Tworzymy nową listę dwukierunkową
        list = DoubleList()
        # Dodajemy kilka elementów do listy
        list.insert_head(Node(1))
        list.insert_head(Node(2))
        list.insert_head(Node(3))
        list.insert_head(Node(4))
        # Sprawdzamy, czy długość listy jest poprawna
        self.assertEqual(4, list.count())
        # Usuwamy ostatni element z listy
        removed_node = list.remove_tail()
        # Sprawdzamy, czy ostatni element został prawidłowo usunięty
        self.assertEqual(1, removed_node.data)
        # Sprawdzamy, czy długość listy została zmniejszona o jeden
        self.assertEqual(3, list.count())

    def test_find_max(self):
        # Tworzymy nową listę dwukierunkową
        list = DoubleList()
        # Dodajemy kilka elementów do listy
        list.insert_head(Node(1))
        list.insert_head(Node(5))
        list.insert_head(Node(3))
        list.insert_head(Node(4))
        # Szukamy maksymalnego elementu na liście
        max_node = list.find_max()
        # Sprawdzamy, czy znaleziony element jest rzeczywiście maksymalnym elementem na liście
        self.assertEqual(5, max_node.data)

    def test_find_min(self):
        # Tworzymy nową listę dwukierunkową
        list = DoubleList()
        # Dodajemy kilka elementów do listy
        list.insert_head(Node(1))
        list.insert_head(Node(5))
        list.insert_head(Node(3))
        list.insert_head(Node(4))
        # Szukamy minimalnego elementu na liście
        min_node = list.find_min()
        # Sprawdzamy, czy znaleziony element jest rzeczywiście minimalnym elementem na liście
        self.assertEqual(1, min_node.data)
        
    def test_remove(self):
        # Tworzymy nową listę dwukierunkową
        list = DoubleList()
        # Dodajemy kilka elementów do listy
        list.insert_head(Node(1))
        list.insert_head(Node(2))
        list.insert_head(Node(3))
        list.insert_head(Node(4))
        # Usuwamy węzeł head (4)
        removed_node = list.remove(list.head)
        # Sprawdzamy, czy węzeł o wartości 4 został prawidłowo usunięty z listy
        self.assertEqual(4, removed_node.data)
        # Sprawdzamy, czy długość listy została zmniejszona o jeden
        self.assertEqual(3, list.count())

    def test_clear(self):
        # Tworzymy nową listę dwukierunkową
        list = DoubleList()
        # Dodajemy kilka elementów do listy
        list.insert_head(Node(1))
        list.insert_head(Node(2))
        list.insert_head(Node(3))
        list.insert_head(Node(4))
        # Czyścimy listę
        list.clear()
        # Sprawdzamy, czy lista jest pusta
        self.assertTrue(list.is_empty())
        # Sprawdzamy, czy długość listy jest równa 0
        self.assertEqual(0, list.count())

if __name__ == "__main__":
    unittest.main()
    
#PS C:\Users\Kamil\Desktop\Studia\Python\zestaw9> python3 doublelist.py -v
#test_count (__main__.TestDoubleList) ... ok
#test_find_max (__main__.TestDoubleList) ... ok
#test_find_min (__main__.TestDoubleList) ... ok
#test_insert_head (__main__.TestDoubleList) ... ok
#test_insert_tail (__main__.TestDoubleList) ... ok
#test_is_empty (__main__.TestDoubleList) ... ok
#test_remove (__main__.TestDoubleList) ... ok
#test_remove_head (__main__.TestDoubleList) ... ok
#test_remove_tail (__main__.TestDoubleList) ... ok
#
#----------------------------------------------------------------------
#Ran 10 tests in 0.003s
#
#OK