'''
Runtime: O(M) where M is the number of elements in the grid 
Correct Answer: 2534
'''

from collections import defaultdict
### setup

# open file
with open('input_5.txt') as f:
# with open('input_four.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

input_rules = []
input_pages = []

for line in lines: 
    if "|" in line:
        input_rules.append(line)
    elif line != "":
        # Convert each string array into an int array
        input_pages.append([int(x) for x in line.split(',')])

### code 
def get_middle_number(arr): 
    mid_index = len(arr) // 2 
    return arr[mid_index]

rules = defaultdict(list)
invalid_updates = []
total = 0

# Reverse all the rules
for input_rule in input_rules:
    x, y = int(input_rule.split("|")[0]), int(input_rule.split("|")[1])
    rules[y].append(x)

# For each item in update, go through and see whether or not it exists in the hashmap
for pages in input_pages:
    nono_nums = set()
    valid = True
    for page in pages:
        # If you see an item in "cannot see next", the update line is not valid
        if page in nono_nums:
            valid = False
            break
        # If it exists, pop all the elements out into a "cannot see next"
        if page in rules:
            nono_nums.update(rules[page])
    if not valid:
        invalid_updates += [pages]
        total += get_middle_number(pages)
print(total)