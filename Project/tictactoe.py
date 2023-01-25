import random
import copy
import math
import pygame

# Kamil Nowak, Projekt Python 2022/2023

# Inicjalizacja pygame
pygame.init()

# Ustawienie rozmiaru ekranu
size = (500, 500)
screen = pygame.display.set_mode(size)

# Ustawienie tytułu okna
pygame.display.set_caption("Kółko i krzyżyk")

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Zmienna przechowująca aktualny znak (kółko lub krzyżyk)
current_sign = 'O'
# Decydowanie kto zaczyna
if random.randint(1,10) % 2 == 1:
    turn = "Gracz" # Zaczyna gracz
else: 
    turn = "CPU"   # Zaczyna komputer
    
firstTurn = turn

# Tablica przechowująca stan gry (puste pole, kółko lub krzyżyk)
game_state = [['', '', ''], ['', '', ''], ['', '', '']]

# Zmienna przechowująca informację o wygranej
winner = None

# Pętla gry
game_over = False

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


pygame.draw.line(screen, white, (200, 100), (200, 400), 5)
pygame.draw.line(screen, white, (300, 100), (300, 400), 5)
pygame.draw.line(screen, white, (100, 200), (400, 200), 5)
pygame.draw.line(screen, white, (100, 300), (400, 300), 5)
pygame.display.flip()


while not game_over:
    font = pygame.font.Font(None, 30) 
    if turn == "Gracz":
        text = font.render("Twoja Tura", True, red)
    else:
        text = font.render("Tura Komputera", True, red)
    fill_rect = pygame.Rect(150, 25, 200, 50)
    screen.fill(white, fill_rect)
    text_rect = text.get_rect(center=(250, 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    

    if turn == "Gracz":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Pobranie pozycji kliknięcia
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0] < 100 or pos[0] > 400 or pos[1] < 100 or pos[1] > 400: 
                    continue # Gracz nie nacisnal na odpowiednie pole
                
                if pos[0] > 100 and pos[0] < 200:
                    column = 0
                elif pos[0] > 200 and pos[0] < 300:
                    column = 1
                elif pos[0] > 300 and pos[0] < 400:
                    column = 2
                else:
                    continue
                if pos[1] > 100 and pos[1] < 200:
                    row = 0
                elif pos[1] > 200 and pos[1] < 300:
                    row = 1
                elif pos[1] > 300 and pos[1] < 400:
                    row = 2
                else:
                    continue
                
                # Sprawdzenie czy pole jest puste
                if game_state[row][column] == '' and turn == "Gracz" and game_over != True:
                    # Rysowanie znaku na ekranie
                    if current_sign == "O":
                        game_state[row][column] = "O"
                        pygame.draw.circle(screen, white, [column*100+150, row*100+150], 40)
                        pygame.draw.circle(screen, black, [column*100+150, row*100+150], 30)
                        current_sign = "X"
                    else:
                        game_state[row][column] = "X"
                        pygame.draw.line(screen, white, (column*100+110, row*100+110), (column*100+190, row*100+190), 5)
                        pygame.draw.line(screen, white, (column*100+190, row*100+110), (column*100+110, row*100+190), 5)
                        current_sign = "O"
                    pygame.display.flip()
                    turn = "CPU"
    elif turn == "CPU":
        print(game_state)
        pygame.time.wait(1000) 
        # Komputer wybiera pole do zaznaczenia za pomocą algorytmu MINMAX
        bestMove = get_best_move(game_state, current_sign)
        column = bestMove[1]
        row = bestMove[0]
            
        print(bestMove)
        #Rysowanie znaku na ekranie
        if current_sign == "O":
            game_state[row][column] = "O"
            pygame.draw.circle(screen, red, [column*100+150, row*100+150], 40)
            pygame.draw.circle(screen, black, [column*100+150, row*100+150], 30)
            current_sign = "X"
        else:
            game_state[row][column] = "X"
            pygame.draw.line(screen, red, (column*100+110, row*100+110), (column*100+190, row*100+190), 5)
            pygame.draw.line(screen, red, (column*100+190, row*100+110), (column*100+110, row*100+190), 5)
            current_sign = "O"
        pygame.display.flip()
        turn = "Gracz"
        print(game_state) 
    # Sprawdzenie wygranej
    winner = check_winner(game_state)
    if winner:
        game_over = True
        if winner == "O" and firstTurn == "Gracz":
            message = "Wygrałeś!"
        elif winner == "X" and firstTurn == "Gracz":
            message = "Przegrałeś!"
        elif winner == "O" and firstTurn == "CPU":
            message = "Przegrałeś!"
        elif winner == "X" and firstTurn == "CPU":
            message = "Wygrałeś!"
        else:
            message = "Remis!"
        pygame.display.flip()

        font = pygame.font.Font(None, 30)
        fill_rect = pygame.Rect(150, 25, 200, 50)
        screen.fill(white, fill_rect)
        text = font.render(message, True, red)
        text_rect = text.get_rect(center=(250, 50))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()


