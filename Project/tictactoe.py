import random
import math
import pygame

# Kamil Nowak, Projekt Python 2022/2023
# Kółko i Krzyżyk z algorytmem MiniMax

# Inicjalizacja pygame
pygame.init()

# Ustawienie rozmiaru ekranu
size = (500, 500)
screen = pygame.display.set_mode(size)

# Ustawienie tytułu okna
pygame.display.set_caption("Tic - Tac - Toe")

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

orange = (230, 156, 27)
lightblue = (225, 243, 249)
blue = (12, 146, 195)

# Zmienna przechowująca aktualny znak (kółko lub krzyżyk)
current_sign = 'O'
# Decydowanie kto zaczyna
if random.randint(1,10) % 2 == 1:
    turn = "Gracz" # Zaczyna gracz
else: 
    turn = "CPU"   # Zaczyna komputer
  
# Zapisuje kto zaczynał gre  
firstTurn = turn

# Tablica przechowująca stan gry (puste pole, kółko lub krzyżyk)
game_state = [['', '', ''], ['', '', ''], ['', '', '']]

# Zmienna przechowująca informację o wygranej
winner = None

# Pętla gry
game_over = False

# Ponowna gra
koniec_gry = 0

# Licznik czasu (10 - 0)
take_time = 0
start_timer = 0
new_timer = 0

# Zmiana koloru przy ostatnich 5 sekundach
designed_color = orange


def check_winner(state):
    # Sprawdzanie wierszy
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '':
            return state[i][0]
    # Sprawdzanie kolumn
    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != '':
            return state[0][i]
    # Sprawdzanie przekątnych
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '':
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '':
        return state[0][2]
    # Sprawdzanie remisu
    if all(state[i][j] != '' for i in range(3) for j in range(3)):
        return 'Tie'
    return None


def minimax(state, depth, isMaximizing, sign):
    result = check_winner(state)
    if sign == 'X':
        sign2 = 'O'
    elif sign == 'O':
        sign2 = 'X'
    if result != None:
        if result == sign2:
            return -10 + depth
        elif result == sign:
            return 10 - depth
        else:
            return 0

    if isMaximizing:
        bestVal = -math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == '':
                    state[i][j] = sign
                    val = minimax(state, depth + 1, False, sign2)
                    state[i][j] = ''
                    bestVal = max(bestVal, val)
        return bestVal
    else:
        bestVal = math.inf
        for i in range(3):
            for j in range(3):
                if state[i][j] == '':
                    state[i][j] = sign2
                    val = minimax(state, depth + 1, True, sign)
                    state[i][j] = ''
                    bestVal = min(bestVal, val)
        return bestVal

def get_best_move(state, sign):
    bestVal = -math.inf
    bestMove = (0, 0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == '':
                state[i][j] = sign
                moveVal = minimax(state, 0, False, sign)
                state[i][j] = ''
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

# Rozrysuj plansze gry
screen.fill(lightblue)
pygame.draw.line(screen, blue, (200, 100), (200, 400), 5)
pygame.draw.line(screen, blue, (300, 100), (300, 400), 5)
pygame.draw.line(screen, blue, (100, 200), (400, 200), 5)
pygame.draw.line(screen, blue, (100, 300), (400, 300), 5)
pygame.display.flip()

while not game_over:
    # Rysuje czyja obecna tura, lub czy gracz chce drugą runde.
    font = pygame.font.Font(None, 30) 
    if koniec_gry == 1:
        # Czytamy czas od poczatku gry i czas obecny. Odejmujemy ich roznice od 10, aby otrzymac licznik
        # idący od 10 do 0. Dla 0 -> koniec gry, dla 5 -> zmiana na kolor ostrzegajacy.
        text = font.render("Try again? "+str(10-(int((new_timer/1000)-(start_timer/1000)))), True, designed_color)
    elif turn == "Gracz":
        text = font.render("Your turn", True, orange)
    else:
        text = font.render("CPU...", True, orange)
    fill_rect = pygame.Rect(150, 25, 200, 50)
    screen.fill(lightblue, fill_rect)
    text_rect = text.get_rect(center=(250, 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
    # Sprawdzam czy gra się skończyła, czekam na decyzje gracza o ponownej grze.
    if koniec_gry == 1:
        if take_time == 1:
            take_time = 0
            start_timer = pygame.time.get_ticks()
        new_timer = pygame.time.get_ticks()
        if 10-(int((new_timer/1000)-(start_timer/1000))) == 5:
            designed_color = red
        elif 10-(int((new_timer/1000)-(start_timer/1000))) == 0:
            # Jesli gracz w ciągu 10 sekund nic nie naciśnie, kończymy gre.
            game_over = True
        winner = None
        game_state = [['', '', ''], ['', '', ''], ['', '', '']]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Resetuje wszystkie ustawienia do początkowych.
                koniec_gry = 0
                current_sign = 'O'
                # Decydowanie kto zaczyna
                if firstTurn == "CPU":
                    turn = "Gracz" # Zaczyna gracz
                else: 
                    turn = "CPU"   # Zaczyna komputer       
                firstTurn = turn
                # Tablica przechowująca stan gry (puste pole, kółko lub krzyżyk)
                screen.fill(lightblue)
                pygame.draw.line(screen, blue, (200, 100), (200, 400), 5)
                pygame.draw.line(screen, blue, (300, 100), (300, 400), 5)
                pygame.draw.line(screen, blue, (100, 200), (400, 200), 5)
                pygame.draw.line(screen, blue, (100, 300), (400, 300), 5)
                designed_color = orange
    # Tura gracza, czekamy aż kliknie na ekranie w odpowiednie pole.
    elif turn == "Gracz":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Pobranie pozycji kliknięcia
                pos = pygame.mouse.get_pos()
                print(pos)
                
                # Zapisujemy ktory rzad i kolumna znajduja sie w miejscu klikniecia gracza
                if pos[0] > 100 and pos[0] < 200:
                    column = 0
                elif pos[0] > 200 and pos[0] < 300:
                    column = 1
                elif pos[0] > 300 and pos[0] < 400:
                    column = 2
                else:
                    continue # Gracz nie nacisnal na odpowiednie pole
                if pos[1] > 100 and pos[1] < 200:
                    row = 0
                elif pos[1] > 200 and pos[1] < 300:
                    row = 1
                elif pos[1] > 300 and pos[1] < 400:
                    row = 2
                else:
                    continue # Gracz nie nacisnal na odpowiednie pole
                
                # Sprawdzenie czy pole jest puste
                if game_state[row][column] == '' and turn == "Gracz" and game_over != True:
                    # Rysowanie znaku na ekranie
                    if current_sign == "O":
                        game_state[row][column] = "O"
                        pygame.draw.circle(screen, blue, [column*100+150, row*100+150], 40)
                        pygame.draw.circle(screen, lightblue, [column*100+150, row*100+150], 30)
                        current_sign = "X"
                    else:
                        game_state[row][column] = "X"
                        pygame.draw.line(screen, blue, (column*100+110, row*100+110), (column*100+190, row*100+190), 5)
                        pygame.draw.line(screen, blue, (column*100+190, row*100+110), (column*100+110, row*100+190), 5)
                        current_sign = "O"
                    pygame.display.flip()
                    # Zmiana tury na komputer
                    turn = "CPU"
    # Tura komputera, czekamy na zwrot algorytmu Minimax
    elif turn == "CPU":
        print(game_state)
        # Czekamy sekunda dla efektu.. Nie jest to konieczne, ale lepiej wygląda
        pygame.time.wait(1000) 
        # Komputer wybiera pole do zaznaczenia za pomocą algorytmu MINMAX
        bestMove = get_best_move(game_state, current_sign)
        column = bestMove[1]
        row = bestMove[0]
            
        print(bestMove)
        # Rysowanie znaku na ekranie
        if current_sign == "O":
            game_state[row][column] = "O"
            pygame.draw.circle(screen, orange, [column*100+150, row*100+150], 40)
            pygame.draw.circle(screen, lightblue, [column*100+150, row*100+150], 30)
            current_sign = "X"
        else:
            game_state[row][column] = "X"
            pygame.draw.line(screen, orange, (column*100+110, row*100+110), (column*100+190, row*100+190), 5)
            pygame.draw.line(screen, orange, (column*100+190, row*100+110), (column*100+110, row*100+190), 5)
            current_sign = "O"
        pygame.display.flip()
        # Zmiana tury na gracza
        turn = "Gracz"
        print(game_state) 
    # Sprawdzenie wygranej
    winner = check_winner(game_state)
    if winner:
        koniec_gry = 1
        take_time = 1
        if winner == "O" and firstTurn == "Gracz":
            message = "You win!"
        elif winner == "X" and firstTurn == "Gracz":
            message = "You lose!"
        elif winner == "O" and firstTurn == "CPU":
            message = "You lose!"
        elif winner == "X" and firstTurn == "CPU":
            message = "You win!"
        else:
            message = "Tie!"
        pygame.display.flip()

        # Wyswietlamy informacje o zwyciezcy lub remisie.
        font = pygame.font.Font(None, 30)
        fill_rect = pygame.Rect(150, 25, 200, 50)
        screen.fill(lightblue, fill_rect)
        text = font.render(message, True, orange)
        text_rect = text.get_rect(center=(250, 50))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2500)


