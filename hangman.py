import os

play_again = True
word_index = 0

def print_man(lives, head_char='O'):
    print('------¬')

    man = [
        [f' {head_char}', '/|\\', '/ \\'],
        [f' {head_char}', '/|\\', '/ '],
        [f' {head_char}', '/|\\', ''],
        [f' {head_char}', '/|', ''],
        [f' {head_char}', ' |', ''],
        [f' {head_char}', '', ''],
        ['', '', '']
    ]

    for line in man[lives]:
        print('|    ', end='')
        print(line)

def print_char(letter):
    print(letter, end=' ')

while play_again:
    words = ['abacateiro', 'preparation','death','combination','appointment','sample','player','society','variety','energy','weakness','atmosphere','management','region','reflection','arrival','profession','secretary','supermarket','disk','professor','tongue','tea','climate','television','phone','owner','dinner','direction','affair','problem','drawer','presence','reputation','restaurant','art','establishment','charity','highway','insect','teaching','guidance','assumption','mode','clothes','farmer','chemistry','wedding','indication','revenue','entry']
    tips = ['It\'s a tree', 'What you do before a challenge', 'After life']
    word = words[word_index]
    tip = tips[word_index]
    mask = [False] * len(word)

    game_is_running = True
    lives = 6
    win = False

    def print_state(head_char='O'):
        os.system('cls')

        # Print hidden word
        for i in range(len(word)):
            if mask[i]:
                print_char(word[i])
            else:
                print_char('_')
        print(f' tip: {tip}      lives: {lives}\n')
        print_man(lives, head_char=head_char)

    while game_is_running:
        print_state()

        user_value = input('> ')

        if user_value == word:
            win = True
            mask = [True] * len(word)
            game_is_running = False
            continue

        hit = False
        for i in range(len(word)):
            if user_value == word[i]:
                hit = True
                mask[i] = True

        if not hit:
            lives -= 1

        if all(mask):
            win = True
            game_is_running = False

        if lives == 0:
            game_is_running = False

    print_state(head_char='X')

    print(f'The word was "{word}"')
    if win:
        print('You Win! :)')
    else:
        print('Loser')

    play_again = input('Play again? [y/n]> ')
    if play_again == 'y':
        play_again = True
    elif play_again == 'n':
        play_again = False

    word_index += 1
