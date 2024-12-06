

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    word_search = f.readlines()

# print(word_search)

def search_left(i, j):
    if j < 3:
        return False

    if word_search[i][j-1] == 'M' and word_search[i][j-2] == 'A' and word_search[i][j-3] == 'S':
        # print(f'Found backwards {i}, {j}')
        return True
    else:
        return False


def search_right(i, j):
    if (j + 3) > (len(word_search[0]) - 1):
        return False

    if word_search[i][j+1] == 'M' and word_search[i][j+2] == 'A' and word_search[i][j+3] == 'S':
        # print(f'Found forwards {i}, {j}')
        return True
    else:
        return False


def search_up(i, j):
    if i < 3:
        return False

    if word_search[i-1][j] == 'M' and word_search[i-2][j] == 'A' and word_search[i-3][j] == 'S':
        # print(f'Found up {i}, {j}')
        return True
    else:
        return False


def search_down(i, j):
    if i + 3 > len(word_search) - 1:
        return False

    if word_search[i+1][j] == 'M' and word_search[i+2][j] == 'A' and word_search[i+3][j] == 'S':
        # print(f'Found down {i}, {j}')
        return True
    else:
        return False


def search_NW(i, j):
    if i < 3 or j < 3:
        return False

    if word_search[i-1][j-1] == 'M' and word_search[i-2][j-2] == 'A' and word_search[i-3][j-3] == 'S':
        # print(f'Found diag up-left {i}, {j}')
        return True
    else:
        return False


def search_SW(i, j):
    if ((i + 3) > (len(word_search) - 1)) or j < 3:
        return False

    if word_search[i+1][j-1] == 'M' and word_search[i+2][j-2] == 'A' and word_search[i+3][j-3] == 'S':
        # print(f'Found diag down-left {i}, {j}')
        return True
    else:
        return False


def search_NE(i, j):
    if i < 3 or ((j + 3) > len(word_search[0]) - 1):
        return False

    if word_search[i-1][j+1] == 'M' and word_search[i-2][j+2] == 'A' and word_search[i-3][j+3] == 'S':
        # print(f'Found diag up-right {i}, {j}')
        return True
    else:
        return False


def search_SE(i, j):
    if ((i + 3) > len(word_search) - 1) or ((j + 3) > len(word_search[0]) - 1):
        return False

    if word_search[i+1][j+1] == 'M' and word_search[i+2][j+2] == 'A' and word_search[i+3][j+3] == 'S':
        # print(f'Found diag down-right {i}, {j}')
        return True
    else:
        return False


def search(i, j):
    search_functions = [
        search_left,
        search_right,
        search_up,
        search_down,
        search_NE,
        search_NW,
        search_SE,
        search_SW,
    ]

    local_count = sum(search(i, j) for search in search_functions)
    return local_count


count = 0
for i in range(len(word_search)):
    for j in range(len(word_search[0])):
        found = False
        char = word_search[i][j]
        if char == 'X':
            local_count = search(i, j)
            count += local_count

print(count) # 2662
