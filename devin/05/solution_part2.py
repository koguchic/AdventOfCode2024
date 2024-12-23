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
def is_valid(update) -> bool:
    queue = deque(update)
    seen = set()
    valid = True
    while queue:
        curr = queue.popleft()
        # Look backward to see if all pages that have already been seen should not come after the current page
        for val in seen:
            if curr in rules:
                if val in rules[curr]:
                    valid = False
                    
        seen.add(curr)

    return valid

# Helper function to shift a value in a list to the left
def shift_left(lst, index):
    if index > 0 and index < len(lst):
        lst[index], lst[index - 1] = lst[index - 1], lst[index]

# Determine which updates are incorrectly ordered and sort them
solution = 0
for update in updates:
    valid = is_valid(update)
    # Disregard all updates that are already ordered properly
    if not valid:
        # From each incorrectly ordered update, add each page of the update to a new "ordered" list
        update = deque(update)
        order = []
        while update:
            curr = update.popleft()
            order.append(curr)
            # If the newly added page causes the list to become unordered, shift it to the left until the list becomes ordered again
            index = order.index(curr)
            while not is_valid(order):
                shift_left(order, index)
                index -= 1

        solution += int(order[len(order)//2])
        
print(solution)