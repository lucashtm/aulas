import os

clear_command = 'cls' if os.name == 'nt' else 'clear'  

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

player1_pieces = 0
player2_pieces = 0

for row in board:
    for place in row:
        if place == player1:
            player1_pieces += 1
            continue
        if place == player2:
            player2_pieces += 1
            continue

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
try_again = False
play_again = False
while True:
    os.system(clear_command)
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
    target_player = player2 if is_player1 else player1
    current_player = player1 if is_player1 else player2
    place = input(f"{'Player 1' if is_player1 else 'Player 2'}> ")
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

    diagonal_x = place_col - piece_col
    diagonal_y = place_row - piece_row
    x_direction = diagonal_x//abs(diagonal_x)
    y_direction = diagonal_y//abs(diagonal_y)

    place_to_check = [piece_col + x_direction, piece_row + y_direction]
    places_to_remove = []
    while place_to_check[0] != place_col and place_to_check[1] != place_row:
        place_value = board[place_to_check[1]][place_to_check[0]]
        if place_value == target_player:
            places_to_remove.append([place_to_check[0], place_to_check[1]])

        if place_value == current_player:
            message = 'Você não pode capturar sua própria peça'
            try_again = True
            break
        place_to_check[0] += x_direction
        place_to_check[1] += y_direction

    for place in places_to_remove:
        board[place[1]][place[0]] = empty
        if is_player1:
            player2_pieces -= 1
        else:
            player1_pieces -= 1

    if len(places_to_remove) > 0:
        diagonals = [
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]

        for diagonal in diagonals:
            place_to_check = [place_col + diagonal[0], place_row + diagonal[1]]
            if board[place_to_check[1]][place_to_check[0]] != target_player:
                continue
            if place_to_check[0] > len(board[0])-1 or place_to_check[0] < 0 or place_to_check[1] > len(board)-1 or place_to_check[1] < 0:
                continue
            place_to_check[0] += diagonal[0]
            place_to_check[1] += diagonal[1]
            if board[place_to_check[1]][place_to_check[0]] == empty:
                play_again = True
    else:
        if (is_player1 and place_row < piece_row) or (not is_player1 and place_row > piece_row):
            message = 'Peças comuns só andam pra frente'
            continue

    if try_again:
        try_again = False
        continue

    board[piece_row][piece_col] = empty
    board[place_row][place_col] = player1 if is_player1 else player2

    if not play_again:
        is_player1 = not is_player1

    play_again = False

    if player1_pieces <= 0:
        print('Player 2 wins!')
        break
    if player2_pieces <= 0:
        print('Player 1 wins!')
        break

