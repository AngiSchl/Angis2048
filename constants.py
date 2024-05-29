# 600 x 600 pixel height and wide
WIDTH, HEIGHT = 600, 600
# 4 times 4 columns and rows in the game board
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH//COLS

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = " "

# Colors of the different squares in rgb
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (245, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 200, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          4096: (237, 190, 37),
          8192: (237, 184, 30),
          'GREY': (128, 128, 128),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'BLACK': (0,0,0),
          'BG': (187, 173, 160)}
