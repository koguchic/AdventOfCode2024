# Day 5 - Part 1
from collections import deque

with open('input.txt', 'r') as file:
    raw = file.readlines()

# Separate the input into two sections - the rules and the updates
rules = dict()
updates = []
second = False
for line in raw:
    if line == '\n':
        second = True
    else:
        if second:
            line = line.strip().split(',')
            updates.append(line)
        else:
            line = line.strip().split('|')
            if line[0] not in rules:
                rules[line[0]] = [line[1]]
            else:
                rules[line[0]].append(line[1])

# Check to see if an update is valid or not
solution = 0
for update in updates:
    queue = deque(update)
    seen = set()
    valid = True
    while queue:
        curr = queue.popleft()
        # Look forward to see if all upcoming pages come after the current page
        for val in queue:
            if curr in rules:
                if val not in rules[curr]:
                    valid = False

        # Look backward to see if all pages that have already been seen should not come after the current page
        for val in seen:
            if curr in rules:
                if val in rules[curr]:
                    valid = False
                    
        seen.add(curr)

    # Add the middle value of the update if the update is valid
    if valid:
        solution += int(update[len(update)//2])   

print(solution)