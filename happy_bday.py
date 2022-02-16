import os, sys
from time import sleep
from art import text2art

font = 'big'
speed = 5
if len(sys.argv) > 1:
    font = sys.argv[1]
if len(sys.argv) > 2:
    speed = int(sys.argv[2])

words = [
    text2art("Parabens", font=font).split('\n'),
    text2art("Yuri", font=font).split('\n'),
    text2art("Feliz", font=font).split('\n'),
    text2art("Aniversario", font=font).split('\n'),
    text2art(":)", font=font).split('\n'),
]

num_lines = len(words[0])

lines = []
for i in range(num_lines):
    line = ''
    for word in words:
        line += word[i]
        line += '   '
    lines.append(line)

columns = 120
init = 0
length = max(map(len, lines))

while True:
    os.system('clear')
    for line in lines:
        for i in range(init, columns+init):
            if i%length < len(line):
                print(line[i%length], end='')
        print()
    init += speed
    sleep(.15)

