# Day 4 - Part 2
with open('input.txt', 'r') as file:
    raw = file.readlines()

# Input crossword: 140 x 140
crossword = []
for line in raw:
    crossword.append(list(line.strip()))

# Checking for valid X-MAS
total = 0
row = 2
column = 2
valid = set(['M', 'S'])
while row < len(crossword):
    middle = crossword[row - 1][column - 1]
    forward = crossword[row][column - 2] + crossword[row - 2][column]
    backward = crossword[row - 2][column - 2] + crossword[row][column]
    combined = forward + backward
    # A valid X-MAS must have a center value of 'A'
    if middle == 'A':
        # Its surround letters must consist of 'M' or 'S'
        if set(combined) == valid:
            # The total number of 'M' and 'S' must total 2 each
            if combined.count('M') == 2 and combined.count('S') == 2:
                # The diagonal must not be the same character, otherwise we end up with 'MAM' or 'SAS'
                if (forward != 'MM' and forward != 'SS') and (backward != 'MM' and backward != 'SS'):
                    total += 1
        
    if column < len(crossword[0]) - 1:
        column += 1
    else:
        column = 2
        row += 1

print(total)