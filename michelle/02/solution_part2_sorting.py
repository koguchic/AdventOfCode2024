'''
The worst-case runtime complexity is approximately O(n * m^3 log m), where n is the number of lines and m is the length of each report.
If I were to remove the log(m) part it would be O(n*m^3)
My answer is 569
'''
from collections import Counter

# read in input.txt
with open('input_two.txt') as f:
    lines = f.readlines()   

# Returns whether or not this report is salvagable by removing one number
def is_salvagable(report):
    # not salvagable if a number occurs more than 3 times
    counted = Counter(report)
    for count in counted.values():
        if count > 3:
            return 0
        
    # remove every number lmao
    for index_to_remove in range(len(report)):
        new_list = [report[i] for i in range(len(report)) if i != index_to_remove]
        if (is_report_valid(new_list, secondpass = True)) == 1:
            return 1
        
    return 0

# Returns whether or not the report is valid
# If it is not valid on its first pass, it will check if it is salvagable
def is_report_valid(report, secondpass = False):
    # quick check that the difference between the first and last number are not too far
    max_distance = 3 * (len(report) - 1)
    if abs(report[0] - report[-1]) > max_distance:
        return 0 if secondpass else is_salvagable(report)

    # must be increasing or decreasing
    # this is o(nlogn) - an optimization could occur here. I optimized my code in solution_part2_no_sorting
    # but this code is beautiful ngl
    increasing = sorted(report)
    decreasing = sorted(report, reverse=True)
    if report != increasing and report != decreasing:
        return 0 if secondpass else is_salvagable(report)

    ## two adjacent levels differ by at least one and at most three
    for i in range(len(report) - 1):
        distance = abs(report[i] - report[i+1])
        if distance == 0 or distance > 3:
            return 0 if secondpass else is_salvagable(report)
    print(report)
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