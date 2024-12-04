# Day 3 - Part 1
import re

# Read the input file
with open('input.txt', 'r') as file:
    raw = file.read()

# Regex for finding the uncorrupted multiply functions
pattern = r'mul\([0-9]+,[0-9]+\)'
total = 0
# Finds all instances of the multiplcation function in the corrupted memory
commands = re.findall(pattern, raw)
# Isolate the numbers found in the multiplcations functions and add the product to the total
for operation in commands:
    operation = operation.split(',')
    operation = [int(operation[0][4::]), int(operation[1][:-1:])]
    total += operation[0] * operation[1]

print(total)