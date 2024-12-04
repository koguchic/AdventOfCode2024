# Day 3 - Part 2
import re

# Read the input file
with open('input.txt', 'r') as file:
    raw = file.read()

# Regex for finding the uncorrupted multiply functions alongside do and don't commands
pattern = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'
total = 0
do = True
# Finds all instances of the regex pattern in the corrupted memory
commands = re.findall(pattern, raw)
for command in commands:
    # Disable mul instructions if 'don't' command found
    if command.startswith('don\'t'):
        do = False
    # Enable mul instructions if 'do' command found
    elif command.startswith('do'):
        do = True
    # Add the product to the total if mul is enabled
    else:
        if do:
            command = command.split(',')
            command = [int(command[0][4::]), int(command[1][:-1:])]
            total += command[0] * command[1]

print(total)