import sys
import time
from pprint import pprint
from copy import deepcopy
from pyfiglet import Figlet


fig = Figlet(font='slant')

OBSTACLE = '#'
CANDIDATE = 'O'
EMPTY = '.'
GUARD = '^'
VISITED = 'X'

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    x = f.readlines()


grid = [list(line.strip()) for line in x]
# pprint(grid)


# Get current position
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == GUARD:
            curr_i, curr_j = [i, j]
            break


def will_loop(curr_i, curr_j, obs_i, obs_j, grid, show_console=True):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_to_sym = {
        (-1, 0): "↑",  # Up
        (0, 1): "→",   # Right
        (1, 0): "↓",   # Down
        (0, -1): "←",  # Left
    }

    # Start orientation as UP
    orientation = 0
    delta_i, delta_j = directions[orientation]

    # Add obstacle
    grid[obs_i][obs_j] = CANDIDATE

    # Keep track of where the guard visits by keeping a copy of the terrain
    visited = deepcopy(grid)
    visited[curr_i][curr_j] = VISITED


    while True:

        # Where we're going?
        new_i = curr_i + delta_i
        new_j = curr_j + delta_j

        # Stay on the map
        still_on_grid = (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0]))
        if still_on_grid:

            next_step = grid[new_i][new_j]
            if next_step in [OBSTACLE, CANDIDATE]:

                # Rotate between 4 orientations
                orientation = (orientation + 1) % len(directions) # Lives on a ring
                delta_i, delta_j = directions[orientation]

            else:
                # Keep it movin'
                curr_i += delta_i
                curr_j += delta_j

                # Mark current_position as visited
                symbol = direction_to_sym[directions[orientation]]

                if show_console:

                    # Clear screen before printing
                    print('\033c', end='')  
                    pprint(visited, stream=sys.stdout)
                    sys.stdout.flush()
                    time.sleep(.005) # Adjust this for desired frequency


                if visited[curr_i][curr_j] == symbol:
                    # We're looping, same place, same direction as before
                    if show_console:
                        # Have to add 1 because we haven't appended yet
                        # This happens outside the function
                        print(fig.renderText(f'INFINITE-LOOP {len(obstacle_candidates)+1}'))
                        print(f"Infinite loop found {obs_i}, {obs_j}")
                        time.sleep(3)

                    # Reset obstacle
                    grid[obs_i][obs_j] = EMPTY
                    return True

                else:
                    visited[curr_i][curr_j] = symbol

        else:
            # Reset obstacle
            grid[obs_i][obs_j] = EMPTY
            return False


print(f'\nStarting at {curr_i}, {curr_j}')
obstacle_candidates = []
for obs_i in range(len(grid)):
    for obs_j in range(len(grid[0])):

        if grid[obs_i][obs_j] not in [OBSTACLE, GUARD]:
            # Simulate movement
            if will_loop(curr_i, curr_j, obs_i, obs_j, grid, False):
                obstacle_candidates.append((obs_i, obs_j))


print(f'Puzzle Answer = {len(obstacle_candidates)}')

