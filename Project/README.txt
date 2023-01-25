----------------------------------------------------------------------
Python 2022 / 2023
Kamil Nowak
Data Prezentacji: 25.01.2023
Tytuł: Gra w kółko i krzyżyk z wykorzystaniem algorytmu 'Minimax'
Plik: tictactoe.py
----------------------------------------------------------------------

-----------------------------Jak grać?--------------------------------
Po uruchomieniu programu, na ekranie wyświetli nam się interfejs
o wymiarach 500x500. Na środku interfejsu rozrysuje nam się plansza
do gry w kółko i krzyżyk. Nad planszą, pojawia się informacja o 
aktualnym ruchu (albo gracz albo komputer). 

Jeżeli tura jest komputera, czekamy aż wykona on swój ruch,
gdy to zrobi, na ekranie w odpowiednim polu
zostanie rozrysowane kółko albo krzyżyk. 

Jeżeli tura jest nasza, musimy nacisnąć myszką na odpowiednie pole,
a na ekranie narysuje nasz znak.

To kto zaczyna rozgrywkę jest decydowane losowo.
Osoba zaczynająca zawsze gra kółko, osoba druga zawsze gra krzyżyk.

Po ukończeniu gry (wszystkie ruchy wyczerpane, lub ktoś wygrał),
nad polem gry zostanie podana informacja o stanie rozgrywki, a
następnie pytanie o chęć ponownej gry. Jeżeli nie chcemy już grać,
wystarczy że wciśniemy krzyżyk w rogu ekranu lub odczekamy 10 sekund.
Jeśli mamy ochotę spróbować ponownie, wystarczy że klikniemy gdziekolwiek
na ekranie, a gra zacznie się ponownie.
----------------------------------------------------------------------

--------------------------Algorytm 'Minimax'--------------------------
Minimax – metoda minimalizowania maksymalnych możliwych strat. 
Alternatywnie można je traktować jako maksymalizację minimalnego zysku. 
Wywodzi się to z teorii gry o sumie zerowej, obejmujących oba przypadki, 
zarówno ten, gdzie gracze wykonują ruchy naprzemiennie, jak i ten,
gdzie wykonują ruchy jednocześnie. 

W naszym programie funkcja wygląda tak: 

`def minimax(state, depth, isMaximizing, sign)`

Przyjmuje jako argumenty: obecny stan gry (tablica 2D z O,X),
Aktualną głębokość, w której przegląda drzewo gry,
To czy chcemy maksymalizować czy minimalizować,
Znak, z którym wchodzimy funkcji (X lub O).

W dwóch pętlach funkcja przegląda sobie wszystkie możliwe ułożenia X i O,
i szuka tego, dla którego wynik będzie najlepszy.
Jeżeli wygramy, to punktacja to 10-depth, czyli karzemy funkcje za głębokość.
Jeżeli przegramy, to punktacja to -10+depth, czyli nagradzamy za głebokość.

To dlatego, że chcemy aby wygrała jak najwcześniej, a przegrał jak najpóźniej.
Za remis zwracamy 0 punktów.

Gdy znajdziemy najlepszy wynik, zapisujemy dla niego najlepszy następny ruch,
i przekazujemy do naszej gry jako ruch komputera.
----------------------------------------------------------------------

----------------------------Jak to działa?----------------------------
Biblioteki z których korzystam:
'pygame' <- do tworzenia interfejsu
'math'   <- do nieskonczonosci w algorytmie minimaxd
'random' <- do losowego wyboru gracza zaczynającego rozgrywke

Zdefiniowane funkcje:
'check_winner(state)'  <- Przekazujemy stan gry, ona zwraca zwycięzce lub None
'minimax(state, depth, isMaximizing, sign)'  <- Nasz algorytm minimax
'get_best_move(state, sign)'  <- funkcja wywołuje minimaxa, zwraca bestMove

Główna pętla gry:
1. Wyświetla obecną ture
2. Jeśli tura gracza, czeka na kliknięcie i pobiera pozycję myszy
3. Jeśli pozycja myszy jest w polu gry, zapisuje kolumne i rząd
4. Zaznacza O lub X, i przekazuje turę komputerowi
5. Komputer wywołuje funkcje get_best_move, czeka na najlepszy ruch
6. Wyrysowujemy ruch komputera i przekazujemy ture graczowi
7. Sprawdzamy czy obecne ułożenie planszy jest końcowe (check_winner)
8. Jeśli tak, wyświetlamy wynik, i sprawdzamy czy gracz chce zagrać ponownie
9. Jeśli gracz w ciągu 10 sekund nie naciśnie niczego na ekranie, kończymy
10. Jeśli kliknie, ustawiamy wartości na domyślne i gra zaczyna się na nowo

Dokładne informacje na temat użytych zmiennych zostały zamieszczone
w komentarzach w kodzie.
----------------------------------------------------------------------





