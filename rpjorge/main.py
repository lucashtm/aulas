import keyboard
import os

# Main game data structure
game = {
    'message': '',
    'running': True,
    'inputs': [],
    'player_char': 'O',
    'floor_char': '.',
    'wall_char': ' ',
    'player_x': 0,
    'player_y': 0,
    'board': [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', ' ', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', ' ', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
}

keyboard.add_hotkey('left', lambda: record_input(game, 'LEFT'))
keyboard.add_hotkey('right', lambda: record_input(game, 'RIGHT'))
keyboard.add_hotkey('up', lambda: record_input(game, 'UP'))
keyboard.add_hotkey('down', lambda: record_input(game, 'DOWN'))

def record_input(game, value):
    game['inputs'].append(value)

def process_inputs(game):
    while len(game['inputs']) <= 0:
        pass
    input_value = game['inputs'].pop(0)
    game['message'] = input_value

    game['board'][game['player_y']][game['player_x']] = game['floor_char'] # Resets player position

    # Updates player position
    if input_value == 'RIGHT':
        if game['player_x'] == len(game['board'][0]) - 1:
            game['player_x'] = 0
        else:
            game['player_x'] += 1
    if input_value == 'LEFT':
        if game['player_x'] == 0:
            game['player_x'] = len(game['board'][0]) - 1
        else:
            game['player_x'] -= 1
    if input_value == 'UP':
        if game['player_y'] == 0:
            game['player_y'] = len(game['board']) - 1
        else:
            game['player_y'] -= 1
    if input_value == 'DOWN':
        if game['board'][game['player_y']+1][game['player_x']] == game['wall_char']:
            pass
        elif game['player_y'] == len(game['board']) - 1:
            game['player_y'] = 0
        else:
            game['player_y'] += 1

def print_screen(game):
    game['board'][game['player_y']][game['player_x']] = game['player_char']
    board = []
    for row in game['board']:
        board.append(''.join(row))
    print('\n'.join(board))
    print(game['message'])

while game['running']:
    os.system('cls') # updates screen every time
    print_screen(game)
    process_inputs(game)
    pass
