'''
Runtime: O(n) where n is the length of the string 
Correct Answer: 77055967
'''

import re
### setup

# open file
with open('input_three.txt') as f:
    lines = f.readlines()   

# merge all three into one line 
merged_input = "".join(lines)

### code

def calculate(str: input) -> int:
    '''
    Given a substring, find all instances of mul(#,#) and return #*# + #*# 
    input: str - "mul(549,158):>!?$,what(),who()mul(429,727)}"
    returns: int - sum of multiplied numbers
    '''
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.findall(regex, input) #("num" , "num")
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


# split on do
split_on_do = merged_input.split("do()")

total = 0
# get everything before the dont
for full_do_string in split_on_do:
    cut_do_string = full_do_string.split("don't()")[0]
    total += calculate(cut_do_string)

print(total)