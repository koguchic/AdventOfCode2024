# Day 1 - Part 1
# Read and clean up the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

input = []
for line in raw:
    line = line.strip()
    line = line.split(' ')
    input.append([int(line[0]), int(line[-1])])

# Separate and sort the input into two different lists
listA = sorted([x[0] for x in input])
listB = sorted([x[1] for x in input])
# Calculate the total distance between each smallest number between both lists
dist = 0
for index in range(len(listA)):
    dist += abs(listA[index] - listB[index])
    
print(dist)