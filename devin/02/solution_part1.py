# Day 2 - Part 1
# Read and clean up the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

reports = []
for line in raw:
    line = line.strip()
    line = line.split(' ')
    line = [int(x) for x in line]
    reports.append(line)

# Determine which reports are safe
safe = 0
for report in reports:
    # Check if the levels in a report are strictly increasing or decreasing
    inOrder = sorted(report)
    if (report == inOrder) or (report == inOrder[::-1]):
        # If it is, check if each adjacent level differs by at least 1 and at most 3
        prev = None
        for index, level in enumerate(report):
            if prev:
                if not (1 <= abs(prev - level) <= 3):
                    break
            
            if index == len(report) - 1:
                safe += 1

            prev = level

print(safe)

    
