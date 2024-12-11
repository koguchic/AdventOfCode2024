from pprint import pprint


EMPTY = '.'
ANTINODE = '#'


def get_tower_locations(tower_freq):
    tower_locations = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == tower_freq:
                tower_locations.append([i, j])

    return tower_locations


def calculate_antinode_pos(tower_1, tower_2):
    delta = [x - y for x, y in zip(tower_2, tower_1)]
    pos1 = [x - y for x, y in zip(tower_1, delta)]
    pos2 = [x + y for x, y in zip(tower_2, delta)]

    return pos1, pos2

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()

grid = [list(row.strip()) for row in x]
pprint(grid)
answer = [['.'] * len(grid[0]) for _ in range(len(grid))]

flattened = []
for row in grid:
    flattened.extend(row)

tower_frequencies = set(flattened).difference(EMPTY)
print(f'There are {len(tower_frequencies)} unique frequencies')
num_antinode = 0
for tower_freq in tower_frequencies:
    tower_locations = get_tower_locations(tower_freq)
    print(f'For frequency {tower_freq} there are {len(tower_locations)} towers')

    # We're doing n choose 2
    for i in range(len(tower_locations)):
        for j in range(i+1, len(tower_locations)):
            tower_1 = tower_locations[i]
            tower_2 = tower_locations[j]

            pos1, pos2 = calculate_antinode_pos(tower_1, tower_2)
            for pos in [pos1, pos2]:
                if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                    answer[pos[0]][pos[1]] = ANTINODE


num_antinode = 0
for i in range(len(answer)):
    for j in range(len(answer[0])):
        c = answer[i][j]
        if c == ANTINODE:
            num_antinode += 1

print(f'Puzzle answer: {num_antinode}') # 313


