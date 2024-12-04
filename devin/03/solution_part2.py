# Day 3 - Part 2
import re

# Read the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

# Regex for finding the uncorrupted multiply functions alongside do and don't commands
pattern = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'

total = 0
# Despite the raw data being broken up into separate lines, do/don't flag needs to carry over to the next line
do = True
for line in raw:
    # Finds all instances of the regex pattern in the corrupted memory
    commands = re.findall(pattern, line)
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