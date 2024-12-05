import re


with open('input.txt', 'r') as f:
    input_string = f.read()

print(input_string)

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, input_string)
pattern_extract = r"mul\((\d+),(\d+)\)"

total = 0
for match in matches:
    m = re.match(pattern_extract, match)
    if m:
        a = int(m.group(1))
        b = int(m.group(2))

        product = a * b
        total += product
    else:
        print("No match found in: ", match)

print(total) # 190604937
