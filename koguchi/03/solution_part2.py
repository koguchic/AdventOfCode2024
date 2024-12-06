import re


with open('input.txt', 'r') as f:
    input_string = f.read()


pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
matches = re.findall(pattern, input_string)
pattern_extract = r"mul\((\d+),(\d+)\)"

total = 0
do = True
for match in matches:
    print(match)
    if "don't" in match:
        do = False
    elif "do" in match:
        do = True
    else:
        m = re.match(pattern_extract, match)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            if do:
                product = a * b
                total += product

print(total) # 82857512
