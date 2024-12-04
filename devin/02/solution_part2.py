# Day 2 - Part 2
# Read and clean up the input file
with open('input.txt', 'r') as file:
    raw = file.readlines()

reports = []
for line in raw:
    line = line.strip()
    line = line.split(' ')
    line = [int(x) for x in line]
    reports.append(line)

# Verifies whther the report is safe or not
def verifySafe(report) -> bool:
    safe = False
    # Check if the levels in a report are strictly increasing or decreasing
    inOrder = sorted(report)
    if (report == inOrder) or (report == inOrder[::-1]):
        # Check if each adjacent level differs by at least 1 and at most 3
        prev = None
        for index, level in enumerate(report):
            if prev:
                if not (1 <= abs(prev - level) <= 3):
                    break
            
            if index == len(report) - 1:
                safe = True

            prev = level

    return safe

# Brute-force approach to save brain power
safe = 0
for report in reports:
    if verifySafe(report):
        safe += 1
    else:
        dampened = False
        for index in range(len(report)):
            temp = report[:index:] + report[index + 1::]
            if verifySafe(temp):
                dampened = True

        if dampened:
            safe += 1

print(safe)