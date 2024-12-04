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
    return within_safe_range


def changes_direction(current: int, previous: int, is_descending: bool) -> bool:
    return (current > previous) == is_descending


def report_is_safe(report: List[int], safety: bool=True) -> bool:
    is_descending = None
    for i in range(1, len(report)):
        previous = report[i-1]
        current = report[i]
        # print(previous, current)

        if not is_within_safe_range(current, previous):
            if safety:
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

        if changes_direction(current, previous, is_descending):
            if safety:
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
        num_safe += 1

print(num_safe) # 404

