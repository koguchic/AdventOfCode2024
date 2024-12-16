from collections import deque
import time
import sys



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
    """Print the topological map with visited nodes highlighted."""
    RESET = "\033[0m"
    VISITED_COLOR = "\033[92m"  # Green for visited cells
    DEFAULT_COLOR = "\033[97m"  # White for non-visited cells
    UNNAVIGABLE_COLOR = "\033[90m"  # Gray for un-navigable cells

    # Clear the console or move the cursor to the top
    sys.stdout.write("\033[H\033[J")  # ANSI escape sequence to clear the screen

    for row_idx, row in enumerate(topological_map):
        for col_idx, value in enumerate(row):
            if (row_idx, col_idx) in visited:
                print(f"{VISITED_COLOR}{value}{RESET}", end=" ")
            elif value == ".":
                print(f"{UNNAVIGABLE_COLOR}.{RESET}", end=" ")
            else:
                print(f"{DEFAULT_COLOR}{value}{RESET}", end=" ")
        print()
    print()

    sys.stdout.flush()
    time.sleep(0.1)


# with open('test_5.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()

# topological_map = [[int(c) for c in row.strip()] for row in x]

topological_map = [
    ['.' if c == '.' else int(c) for c in row.strip()] 
    for row in x
]

# print_colored_map(topological_map, set())
trail_heads = []

for i in range(len(topological_map)):
    for j in range(len(topological_map[0])):
        if topological_map[i][j] == 0:
            trail_heads.append((i, j))


trail_head_rating_sum = 0
while trail_heads:
    current = trail_heads.pop()
    queue = deque()
    print(f'Starting on {current}')
    queue.append(current)
    visited = set()

    num_paths = 0
    while queue:
        pos = queue.pop()

        # if pos in visited:
        #     continue

        visited.add(pos)
        # print_colored_map(topological_map, visited)

        neighbors = get_neighbors(pos)
        i, j = pos
        current_altitude = topological_map[i][j]

        for neighbor in neighbors:
            i_n, j_n = neighbor
            neigh_alt = topological_map[i_n][j_n]

            # TODO: Delete
            if neigh_alt == ".":
                continue


            if neigh_alt == (current_altitude + 1):
                queue.append(neighbor)

                if neigh_alt == 9:
                    num_paths += 1

    print(f'Path Rating: {num_paths}')
    trail_head_rating_sum += num_paths

print(f'Answer: {trail_head_rating_sum}')

