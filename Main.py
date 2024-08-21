import pygame
import random
pygame.init()

# initial set-up
from constants import WIDTH, HEIGHT, colors, game_over, spawn_new, init_count, direction
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)
score = 0
file = open('high_score.txt', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high


# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]

# draw background for the board
def draw_board():
    pygame.draw.rect(screen, colors['BG'], [0, 0, 500, 500], 0, 3)
    score_text = font.render(f'Score: {score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (10, 510))
    screen.blit(high_score_text, (10, 550))

# Randomly creating new pieces in a not occupied field:
def new_pieces(board):
    count = 0
    board_full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        board_full = True
    return board, board_full

#draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 8192:
                color = colors[value]
            else:
                color = colors['BLACK']
            pygame.draw.rect(screen, color, [j * 115 + 30, i * 115 + 30, 85, 85], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 115 + 73, i * 115 + 73))
                screen.blit(value_text, text_rect)

# Draw over function to build the "GAME OVER and RESTART" slogan at the end of the game.
def draw_over():
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100],0, 10)
    game_over_text = font.render('Game Over!', True, 'white')
    game_over_text1 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text, [130, 65])
    screen.blit(game_over_text1, [70, 105])

# Take your turn based on direction
def take_turn(direc, board):
    # List of merged will take note which row/colum combination was already merged.
    # As each position can only merge once per click.
    merged = [[False for _ in range(4)] for _ in range(4)]
    global score
    if direc == "UP":
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift -1][j] \
                            and not merged[i - shift][j]:
                        board[i - shift - 1][j] *= 2
                        score += board[i - shift - 1][j]
                        board[i- shift][j] = 0
                        merged[i - shift - 1][j] = True


    elif direc == "DOWN":
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift +=1
                if shift > 0:
                    board[2- i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board [2 -i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                    and not merged[2 - i + shift][j]:
                         board[3 - i + shift][j] *= 2
                         score += board[3 - i + shift][j]
                         board[2 - i + shift][j]  = 0
                         merged[3 - i - shift][j] = True


    elif direc == "LEFT":
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                    if shift > 0:
                        board[i][j - shift] = board[i][j]
                        board[i][j] == 0
                    if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] and not merged[i][j - shift]:
                        board[i][j - shift - 1] *= 2
                        score += board[i][j - shift - 1]
                        board[i][j - shift] = 0
                        merged[i][j - shift -1] = True

    elif direc == "RIGHT":
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if (board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]):
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True


    return board


# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(colors['GREY'])
    draw_board()
    draw_pieces(board_values)

    if spawn_new or init_count < 2:
        board_values, game_over = new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != "":
        board_values = take_turn(direction, board_values)
        direction = ""
        spawn_new = True
    if game_over:
        draw_over()
        if high_score > init_high:
            file = open('high_score.txt', 'w')
            file.write(f'{high_score}')
            file.close()
            init_high = high_score


    #Check if any events have taken place
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP and not game_over:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'

            if game_over:
                # Click enter to restart the game after you lost:
                if event.key == pygame.K_RETURN:
                    board_values = [[0 for _ in range(4)] for _ in range(4)]
                    spawn_new = True
                    init_count = 0
                    score = 0
                    direction = ''
                    game_over = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if score > high_score:
        high_score = score

    pygame.display.flip()

pygame.quit()
