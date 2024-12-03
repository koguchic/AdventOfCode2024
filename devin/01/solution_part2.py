# Day 1 - Part 2
# Read and clean up the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

input = []
for line in raw:
    line = line.strip()
    line = line.split(' ')
    input.append([int(line[0]), int(line[-1])])

# Separate the input into two different lists
listA = [x[0] for x in input]
listB = [x[1] for x in input]
# Create a count of each value that exists in listB
seen = dict()
for val in listB:
    if val not in seen:
        seen[val] = 1
    else:
        seen[val] += 1

# Calculate the total similarity between the two lists
similarity = 0
for val in listA:
    if val in seen:
        similarity += val * seen[val]

print(similarity)