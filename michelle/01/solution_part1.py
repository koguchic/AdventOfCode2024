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
total = 0

# sort the two lists
one.sort()
two.sort()

# find the differences between each index
if len(one) != len(two):
    print("lists are not equal in length")
else:
    for i in range(len(one)):
        # add to total
        total += abs(one[i] - two[i])

print(total)