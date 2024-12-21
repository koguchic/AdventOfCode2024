from pprint import pprint
from collections import deque, defaultdict


with open('input.txt', 'r') as f:
    x = f.readlines()

land = [list(row.strip()) for row in x]
pprint(land)

neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    area = 1
    perimeter = 0
    target_plant_type = land[i][j]
    visited.add((i, j))

    while queue:
        i, j = queue.popleft()

        plant_type = land[i][j]
        if plant_type == target_plant_type:
            if i == 0 or i == len(land) - 1:
                perimeter += 1
            if j == 0 or j == len(land[0]) - 1:
                perimeter += 1

        for delta_x, delta_y in neighbors:
            x = i+delta_x
            y = j+delta_y

            if 0 <= x < len(land) and 0 <= y < len(land[0]):
                plant_type = land[x][y]

                if plant_type != target_plant_type:
                    perimeter += 1

                if plant_type == target_plant_type and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y))
                    area += 1

    return area, perimeter


seen_area = defaultdict(list)
seen_peri = defaultdict(list)
visited = set()

for i in range(len(land)):
    for j in range(len(land[0])):
        current_plant_type = land[i][j]
        if (i, j) not in visited:
            area, perimeter = bfs(i, j)
            seen_area[current_plant_type].append(area)
            seen_peri[current_plant_type].append(perimeter)

pprint(seen_area)
pprint(seen_peri)

price = 0
for plant_type, perimeters in seen_peri.items():
    areas = seen_area[plant_type]
    for a, p in zip(areas, perimeters):
        price += a*p

print(price)

