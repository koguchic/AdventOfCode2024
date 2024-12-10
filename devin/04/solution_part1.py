# Day 4 - Part 1
import numpy as np

with open('input.txt', 'r') as file:
    raw = file.readlines()

# Input crossword: 140 x 140
crossword = []
for line in raw:
    crossword.append(list(line.strip()))

crossword = np.array(crossword)
total = 0
# Checking each row
for row in crossword:
    row = ''.join(row)
    total += row.count('XMAS')
    total += row.count('SAMX')

# Checking diagonals
row = 3
column = 3
while row < len(crossword):
    forward = crossword[row][column - 3] + crossword[row - 1][column - 2] + crossword[row - 2][column - 1] + crossword[row - 3][column]
    backward = crossword[row - 3][column - 3] + crossword[row - 2][column - 2] + crossword[row - 1][column - 1] + crossword[row][column]
    if forward == 'XMAS' or forward == 'SAMX':
        total += 1

    if backward == 'XMAS' or backward == 'SAMX':
        total += 1

    if column < len(crossword[0]) - 1:
        column += 1
    else:
        column = 3
        row += 1

# Checking each column
crossword = np.transpose(crossword)
print(crossword)
for column in crossword:
    column = ''.join(column)
    total += column.count('XMAS')
    total += column.count('SAMX')

print(total)