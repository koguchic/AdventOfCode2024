from typing import List


def parse_lines(lines: List) -> List:
    location_ids = []
    for line in lines:
        line = line.strip()
        location_id_a, location_id_b = line.split('   ')
        location_id_a, location_id_b = int(location_id_a), int(location_id_b)
        location_ids.append((location_id_a, location_id_b))

    return location_ids


with open('input.txt', 'r') as f:
    raw_input = f.readlines()
    location_ids = parse_lines(raw_input)

# nlogn
location_a = sorted([location[0] for location in location_ids])
location_b = sorted([location[1] for location in location_ids])

# n
distances = 0
for a, b in zip(location_a, location_b):
    distances += max(a - b, b - a)

print(distances)

