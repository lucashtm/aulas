word = 'abacateiro'
mask = [False, False, False, False, False, False, False, False, False, False]

game_is_running = True
lives = 6
win = False

while game_is_running:
    letter = input('> ')

    for i in range(len(word)):
        if letter == word[i]:
            mask[i] = True

    if not letter in word:
        lives -= 1
        print(f'The letter {letter} is not in the word')

    if all(mask):
        win = True
        game_is_running = False

    if lives == 0:
        game_is_running = False

if win:
    print('You Win! :)')
else:
    print('Loser')
