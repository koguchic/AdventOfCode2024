# Day 3 - Part 1
import re

# Read the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

# Regex for finding the uncorrupted multiply functions
pattern = r'mul\([0-9]+,[0-9]+\)'

total = 0
for line in raw:
    # Finds all instances of the multiplcation function in the corrupted memory
    commands = re.findall(pattern, line)
    # Isolate and mutliply the numbers found in valid multiply functions
    for operation in commands:
        operation = operation.split(',')
        operation = [int(operation[0][4::]), int(operation[1][:-1:])]
        total += operation[0] * operation[1]

print(total)
