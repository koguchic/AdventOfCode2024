from typing import List


def parse_lines(lines: List):
    location_ids_a = []
    location_ids_b = []
    for line in lines:
        line = line.strip()
        location_id_a, location_id_b = line.split('   ')
        location_id_a, location_id_b = int(location_id_a), int(location_id_b)
        #location_ids.append((location_id_a, location_id_b))
        
        location_ids_a.append(location_id_a)
        location_ids_b.append(location_id_b)

    return location_ids_a, location_ids_b #location_ids


with open('input.txt', 'r') as f:
    raw_input = f.readlines()
    location_ids_a, location_ids_b = parse_lines(raw_input)
    
location_ids_a.sort()
location_ids_b.sort()

#credit to christian thx
diff = [abs(a - b) for a,b in zip(location_ids_a, location_ids_b)]

print(sum(diff))