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
    # Why was this so awkwardly hard for me lol
    if current > previous:
        if is_descending:
            # print(f"swapped directions {previous} {current}")
            return True
        else:
            return False

    else: # current < previous
        if is_descending:
            return False
        else:
            # print(f"swapped directions {previous} {current}")
            return True


def report_is_safe(report: List[int], safety: bool=True) -> bool:
    print(report)
    is_descending = None
    for i in range(1, len(report)):
        previous = report[i-1]
        current = report[i]
        # print(previous, current)

        if not is_within_safe_range(current, previous):
            print(f'Breaking unsafe range {previous} {current}')
            if safety:
                print('Safety blown')
                safety = False
                tmp1 = report.copy()
                tmp2 = report.copy()
                del tmp1[i]
                del tmp2[i-1]
                return report_is_safe(tmp1, False) or report_is_safe(tmp2, False)
            else:
                break

        if is_descending is None:
            is_descending = current < previous
            if is_descending:
                print(f'This run is descending')
            else:
                print(f'This run is ascending')

        if changes_direction(current, previous, is_descending):
            print('Breaking change direction')
            if safety:
                print('Safety blown')
                safety = False
                tmp1 = report.copy()
                tmp2 = report.copy()
                tmp3 = report.copy()
                del tmp1[i]
                del tmp2[i-1]
                del tmp3[i-2]
                return report_is_safe(tmp1, False) or report_is_safe(tmp2, False) or report_is_safe(tmp3, False)
            else:
                break

    else:
        return True

    return False


# O(num_reports*levels^2)

# reports = [
    # [7, 6, 4, 2, 1,],
    # [1, 2, 7, 8, 9,],
    # [9, 7, 6, 2, 1,],
    # [1, 3, 2, 4, 5,],
    # [8, 6, 4, 4, 1,],
    # [1, 3, 6, 7, 9,],
#     [12, 10, 12, 14, 15, 16, 19, 22]
# ]

num_safe = 0
for report in reports:
    if report_is_safe(report):
        print('REPORT SAFE\n\n')
        num_safe += 1
    else:
        print('REPORT NOT SAFE\n\n')

print(num_safe) # 404

