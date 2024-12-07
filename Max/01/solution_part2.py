from typing import List
from collections import defaultdict


def parse_lines(lines: List):
    location_ids_a = defaultdict(int)
    location_ids_b = defaultdict(int)
    
    for line in lines:
        line = line.strip()
        location_id_a, location_id_b = line.split('   ')
        location_id_a, location_id_b = int(location_id_a), int(location_id_b)
        
        location_ids_a[location_id_a] += 1
        location_ids_b[location_id_b] += 1
        
        #location_ids_a.append(location_id_a)
        #location_ids_b.append(location_id_b)
    return location_ids_a, location_ids_b #location_ids


with open('input.txt', 'r') as f:
    raw_input = f.readlines()
    location_ids_a, location_ids_b = parse_lines(raw_input)
    
running_sum = 0

for id_a, val in location_ids_a.items():
    running_sum += location_ids_b[id_a] * id_a * val
    
print (running_sum)