import os

player1 = 'O'
player2 = 'X'
queen = '@'

empty = ' '

board = [
    [empty, player1, empty, player1, empty, player1, empty, player1],
    [player1, empty, player1, empty, player1, empty, player1, empty],
    [empty, player1, empty, player1, empty, player1, empty, player1],
    [empty] * 8,
    [empty] * 8,
    [player2, empty, player2, empty, player2, empty, player2, empty],
    [empty, player2, empty, player2, empty, player2, empty, player2],
    [player2, empty, player2, empty, player2, empty, player2, empty],
]

def print_board(board, message):
    row_indexes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    col_indexes = '      1   2   3   4   5   6   7   8  '
    row_delimiter = '    +---+---+---+---+---+---+---+---+'
    print(row_delimiter)
    for i in range(len(board)):
        print(f'{row_indexes[i]}   | ', end='')
        for j in range(len(board[i])):
            if j != 0:
                print(' | ', end='')
            print(board[i][j], end='')
        print(' |')
        print(row_delimiter)
    print(f'\n{col_indexes}')
    print(f'\n{message}\n\n')

def get_board_coords(coord):
    coords = list(coord)
    row = ord(coords[0]) - ord('a')
    col = int(coords[1]) - 1
    return row, col

def get_board_value(board, coord):
    row, col = get_board_coords(coord)
    return board[row][col]

message = ''
is_player1 = True
while True:
    os.system('cls')
    print_board(board, message)
    message = ''
    piece = input(f"{'Player 1' if is_player1 else 'Player 2'}> ")
    piece_value = get_board_value(board, piece)
    if piece_value == empty:
        message = 'Não há peças nessa casa'
        continue
    if (is_player1 and piece_value != player1) or (not is_player1 and piece_value != player2):
        message = 'Escolha uma peça sua'
        continue
    place = input('> ')
    place_value = get_board_value(board, place)
    piece_row, piece_col = get_board_coords(piece)
    place_row, place_col = get_board_coords(place)

    distance = abs(place_row - piece_row) + abs(place_col - piece_col)

    if abs(place_row - piece_row) != abs(place_col - piece_col):
        message = 'Você só pode se mover em diagonais'
        continue

    if distance > 4:
        message = 'Não pode ir tão longe'
        continue

    if place_value != empty:
        message = 'Essa casa já está ocupada'
        continue

    if (is_player1 and place_row < piece_row) or (not is_player1 and place_row > piece_row):
        message = 'Peças comuns só andam pra frente'
        continue

    board[piece_row][piece_col] = empty
    board[place_row][place_col] = player1 if is_player1 else player2
    is_player1 = not is_player1



