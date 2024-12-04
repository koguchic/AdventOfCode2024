from typing import List


def parse_lines(lines: List) -> List:
    reports = []
    for line in lines:
        line = line.strip()
        report = line.split(' ')
        reports.append([int(level) for level in report])

    return reports


with open('input.txt', 'r') as f:
    raw_input = f.readlines()
    reports = parse_lines(raw_input)

# print(reports)


def is_within_safe_range(current: int, previous: int) -> bool:
    within_safe_range = 1 <= abs(current - previous) <= 3
    # if not within_safe_range:
    #     print(f'difference: {abs(current - previous)}')
    return within_safe_range


def changes_direction(current: int, previous: int, is_descending: bool) -> bool:
    return (current > previous) == is_descending


def report_is_safe(report):
    is_descending = None
    for i in range(1, len(report)):
        previous = report[i-1]
        current = report[i]
        # print(previous, current)

        if not is_within_safe_range(current, previous):
            # print('Breaking unsafe range')
            break

        if is_descending is None:
            is_descending = current < previous
            # print(f'This run is descending: {is_descending}')

        if changes_direction(current, previous, is_descending):
            # print('Breaking change direction')
            break
    else:
        return True

    return False


# O(num_reports*levels)
num_safe = 0
for report in reports:
    print(report)

    if report_is_safe(report):
        num_safe += 1

print(num_safe)

