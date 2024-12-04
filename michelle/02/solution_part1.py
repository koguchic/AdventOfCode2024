### setup ###

# read in input.txt
with open('input_two.txt') as f:
    lines = f.readlines()   

### code
def is_report_valid(report):
    # quick check that the difference between the first and last number are not too far
    max_distance = 3 * (len(report) - 1)
    if abs(report[0] - report[-1]) > max_distance:
        return 0

    # must be increasing or decreasing
    # this is o(nlogn) - an optimization could occur here
    # but the code is beautiful ngl
    increasing = sorted(report)
    decreasing = sorted(report, reverse=True)
    if report != increasing and report != decreasing:
        return 0

    ## two adjacent levels differ by at least one and at most three
    for i in range(len(report) - 1):
        distance = abs(report[i] - report[i+1])
        if distance == 0 or distance > 3:
            return 0
        
    return 1

total_safe = 0
for line in lines:
    line = line.strip()
    str_report = line.split(" ")
    report = [int(item) for item in str_report]

    total_safe += is_report_valid(report)

print(total_safe)


""" 
Knowledge Notes (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

Christian taught me what a for else looks like in case you dont want to implement
the solution in a is_report_valid function! It looks like this:

for i in range(len(report) - 1):
    distance = abs(report[i] - report[i+1])
    if distance == 0 or distance > 3:
        break
else:
    total_safe += 1


Pretty awesome!
"""