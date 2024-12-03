from typing import List
from collections import Counter


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


# O(n)
location_a = [location_id[0] for location_id in location_ids]
location_b = [location_id[1] for location_id in location_ids]
frequency_b = Counter(location_b)
# print(frequency_b)

# O(n)
similarity_score = 0
for location_id in location_a:
    if location_id in frequency_b:
        similarity_score += location_id * frequency_b[location_id]

print(similarity_score) # 23963899

