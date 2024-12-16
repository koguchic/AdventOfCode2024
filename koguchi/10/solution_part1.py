from collections import deque
from pprint import pprint


# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()

topological_map = [[int(c) for c in row.strip()] for row in x]

pprint(topological_map)
trail_heads = []

for i in range(len(topological_map)):
    for j in range(len(topological_map[0])):
        if topological_map[i][j] == 0:
            trail_heads.append((i, j))


def get_neighbors(pos):
    i, j = pos

    up = (i-1, j)
    down = (i+1, j)
    left = (i, j-1)
    right = (i, j+1)

    neighbors = []
    for neighbor in [up, down, left, right]:
        i, j = neighbor
        if 0 <= i < len(topological_map) and 0 <= j < len(topological_map[0]):
            neighbors.append(neighbor)

    return neighbors


def print_colored_map(topological_map, visited):
    # ANSI escape codes for colors
    RESET = "\033[0m"
    VISITED_COLOR = "\033[92m"  # Green for visited cells
    DEFAULT_COLOR = "\033[97m"  # White for non-visited cells

    for row_idx, row in enumerate(topological_map):
        for col_idx, value in enumerate(row):
            if (row_idx, col_idx) in visited:
                print(f"{VISITED_COLOR}{value}{RESET}", end=" ")  # Highlight visited
            else:
                print(f"{DEFAULT_COLOR}{value}{RESET}", end=" ")  # Default color
        print()

trail_head_score_sum = 0
while trail_heads:
    current = trail_heads.pop()
    queue = deque()
    print(f'Starting on {current}')
    queue.append(current)
    visited = set()
    while queue:
        pos = queue.popleft()

        if pos in visited:
            continue

        visited.add(pos)
        neighbors = get_neighbors(pos)

        i, j = pos
        current_altitude = topological_map[i][j]
        # print(f'Currently at pos {pos} - alt. {current_altitude}')
        for neighbor in neighbors:
            i_n, j_n = neighbor
            neigh_alt = topological_map[i_n][j_n]

            if neigh_alt == (current_altitude + 1):
                queue.append(neighbor)


    # print_colored_map(topological_map, visited)
    trail_head_score = 0
    for pos in visited:
        i, j = pos
        altitude = topological_map[i][j]
        if altitude == 9:
            trail_head_score += 1

    print(f'Trailhead Score: {trail_head_score}')
    trail_head_score_sum += trail_head_score

print(f'Trailhead Score Sum: {trail_head_score_sum}')
