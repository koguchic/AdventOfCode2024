### setup ###

# read in input.txt
with open('input.txt') as f:
    lines = f.readlines()

one = []
two = []

for line in lines:
    line = line.strip()
    nums = line.split("   ")
    one.append(int(nums[0]))
    two.append(int(nums[1]))

### code ###

from collections import Counter

# hash the right table with the number of times it occurs
hashmap = Counter(two)

# count similarities 
total = 0
for num in one:
    total += num * hashmap[num]

print(total)