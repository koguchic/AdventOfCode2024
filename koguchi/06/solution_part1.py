from pprint import pprint


OBSTACLE = '#'
GUARD = '^'
VISITED = 'X'

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()


grid = [list(line.strip()) for line in x]
pprint(grid)


# Get current position
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == GUARD:
            curr_i, curr_j = [i, j]
            break


print(f'\nStarting at {curr_i}, {curr_j}')

# Keep track of where the guard visits by keeping a copy of the terrain
visited = grid.copy()
visited[curr_i][curr_j] = VISITED

v = set()
v.add((curr_i, curr_j))

# Simulate movement
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
orientation = 0
delta_i, delta_j = directions[orientation]


while True:

    # Where we're going?
    new_i = curr_i + delta_i
    new_j = curr_j + delta_j

    # Stay on the map
    still_on_grid = (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0]))
    if still_on_grid:

        next_step = grid[new_i][new_j]
        if next_step == OBSTACLE:
            print(f"Collision at {new_i}, {new_j}")

            # Rotate between 4 orientations
            orientation = (orientation + 1) % 4 # lives on a ring
            delta_i, delta_j = directions[orientation]

        else:
            # Keep it movin'
            curr_i += delta_i
            curr_j += delta_j

            # Mark current_position as visited
            visited[curr_i][curr_j] = VISITED
            v.add((curr_i, curr_j))

    else:
        break


print('\n')
pprint(visited)

# Count em both ways
count = 0
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if visited[i][j] == VISITED:
            count += 1

print(f'\nPuzzle Answer: {count}')
print(f'\nPuzzle Answer: {len(v)}')

