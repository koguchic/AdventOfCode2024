'''
Runtime: O(M) where M is the number of elements in the grid 
Correct Answer: 2534
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
keys = ["XMAS", "SAMX"]

hcount = 0
vcount = 0 
rdiagcount = 0
ldiagcount = 0 

# horizontal
for line in lines:
    for key in keys:
        count += line.count(key)
hcount = count

up_boundry = 4 - 1
down_boundry = max_y - (len("XMAS") - 1)
right_boundry = max_x - (len("XMAS") - 1)
left_boundry = 4 - 1

for x in range(len(lines)):
    for y in range(len(lines[0])):
        # look vertical
        if x >= 3:
            substring = ""
            substring += grid[x][y]
            substring += grid[x - 1][y]
            substring += grid[x - 2][y]
            substring += grid[x - 3][y]
            if substring in keys:
                count += 1
                vcount += 1
        # look rdiagonal
        if y <= down_boundry and x <= right_boundry: # stop before going to far down or too far right
            substring = ""
            substring += grid[x][y]
            substring += grid[x + 1][y + 1]
            substring += grid[x + 2][y + 2]
            substring += grid[x + 3][y + 3]
            if substring in keys:
                count += 1
                rdiagcount += 1
        # # look ldiagonal
        if y <= down_boundry and x >= left_boundry:
            substring = ""
            substring += grid[x][y]
            substring += grid[x - 1][y + 1]
            substring += grid[x - 2][y + 2]
            substring += grid[x - 3][y + 3]
            if substring in keys:
                count += 1
                ldiagcount += 1

print("hcount", hcount)
print("vcount", vcount)
print("rdiagcount", rdiagcount)
print("ldiagcount", ldiagcount)
print(count) # 2534
