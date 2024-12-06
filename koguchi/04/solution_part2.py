import numpy as np


KERNEL_SIZE = 3
PADDING = KERNEL_SIZE // 2

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    word_search = f.readlines()

word_search = [list(line.strip()) for line in word_search]
word_search = np.array(word_search)

print(word_search)

def valid_padding(i, j):
    horizontal_bound = PADDING <= j < word_search.shape[1] - PADDING
    vertical_bound = PADDING <= i < word_search.shape[0] - PADDING
    return horizontal_bound and vertical_bound

def get_patch(i, j):
    patch = word_search[i-PADDING:i+PADDING+1, j-PADDING:j+PADDING+1]
    return patch

def check_patch(patch):
    if patch[1, 1] != 'A':
        return False

    if patch[0, 0] == 'M' and patch[2, 2] == 'S':
        if patch[0, 2] == 'M' and patch[2, 0] == 'S':
            return True
        elif patch[0, 2] == 'S' and patch[2, 0] == 'M':
            return True
        else:
            return False
    elif patch[0, 0] == 'S' and patch[2, 2] == 'M':
        if patch[0, 2] == 'M' and patch[2, 0] == 'S':
            return True
        elif patch[0, 2] == 'S' and patch[2, 0] == 'M':
            return True
        else:
            return False
    else:
        return False


count = 0
for i in range(word_search.shape[0]):
    for j in range(word_search.shape[1]):
        if not valid_padding(i, j):
            continue

        patch = get_patch(i, j)
        if check_patch(patch):
            count += 1

print(count) # 2034

