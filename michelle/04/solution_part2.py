'''
Runtime: O(M) where M is the number of elements in the grid 
Correct Answer: 1866
'''

import re
### setup

# open file
with open('input_four.txt') as f:
# with open('input_four.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
 
### code
grid = lines
count = 0

max_x = len(lines) - 1 
max_y = len(lines[0]) - 1
keys = ["MAS", "SAM"]
word_len = len("MAS")
up_boundry = word_len - 1
down_boundry = max_y - (word_len - 1)
right_boundry = max_x - (word_len - 1)
left_boundry = word_len - 1

for x in range(len(lines)):
    for y in range(len(lines[0])):
        rsubstring = ""
        lsubstring = ""
        if x >= left_boundry and y <= down_boundry:
            # look rdiagonal
            rsubstring += grid[x - 2][y]
            rsubstring += grid[x - 1][y + 1]
            rsubstring += grid[x][y + 2]
            # # look ldiagonal
            lsubstring += grid[x][y]
            lsubstring += grid[x - 1][y + 1]
            lsubstring += grid[x - 2][y + 2]
            if lsubstring in keys and rsubstring in keys:
                count += 1

print(count) # 2534