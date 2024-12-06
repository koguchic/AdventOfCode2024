'''
Runtime: O(n) where n is the length of the string 
Correct Answer: 153469856
'''

import re
### setup

# open file
with open('input_three.txt') as f:
    lines = f.readlines()   

# merge all three into one line 
merged_input = "".join(lines)

### code

# regex to array
regex = r"mul\((\d+),(\d+)\)"
matches = re.findall(regex, merged_input)  #("num" , "num")

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])
print(total)